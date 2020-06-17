"""
  Space_coaster_player for V3 software
  
  This version reads telemetry data from a CSV file
  Attitude information is read from this file synced to UDP frames
  sent by SpaceCoaster on port 10009 (data in coaster msg frames is ignored)
"""

import sys
import socket
from math import radians, degrees
from threading import Thread, Lock
import time
try:
    from queue import Queue
except ImportError:
    from Queue import Queue

import traceback
import csv,os
import win32gui

from space_coaster_gui_defs import *

import logging
log = logging.getLogger(__name__)

import ctypes # for mouse
import numpy as np  # for scaling telemetry data

 
sys.path.insert(0, '../common')
from serial_remote import SerialRemote
from udp_remote import UdpRemote
import gui_utils as gutil

class State:
    initializing, waiting, ready, running, completed = list(range(0,5))

class RideState:  # only used to contol LED in remote
    DISABLED, READY_FOR_DISPATCH, RUNNING, PAUSED, EMERGENCY_STOPPED, RESETTING = list(range(6))
    
ride_state_str = {'Disabled','Ready for Dispatch','Running','Paused','Emergency Stopped','Resetting'}

class ConnectionException(Exception):
    pass

class InputInterface(object):
    USE_GUI = True  # set True if using tkInter
    USE_UDP_MONITOR = False
    
    def set_focus(self, window_class=None, window_title=None):
        guiHwnd = win32gui.FindWindow(window_class,window_title)
        log.debug("gui Hwnd= %d", guiHwnd)
        win32gui.SetForegroundWindow(guiHwnd)
        
    def left_mouse_click(self):
        #print "left mouse click"
        ctypes.windll.user32.SetCursorPos(100, 20)
        #self.set_focus("UnityWndClass")
        ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
        ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
        #self.set_focus("TkTopLevel")
   
    def right_mouse_click(self):
        ctypes.windll.user32.SetCursorPos(100, 20)
        ctypes.windll.user32.mouse_event(8, 0, 0, 0,0) # right down
        ctypes.windll.user32.mouse_event(16, 0, 0, 0,0) # right up


    def __init__(self, sleep_func, is_local_client = False):
        self.sleep_func = sleep_func
        self.is_local_client = is_local_client
        self.log = None
        self.is_normalized = True
        self.expect_degrees = False # convert to radians if True
        self.HOST = "localhost"
        self.PORT = 10009
        if self.is_normalized:
            log.info('Platform Input is UDP with normalized parameters')
        else:
            log.info('Platform Input is UDP with realworld parameters')
   
        self.max_values = [80, 80, 80, 0.4, 0.4, 0.4]
        self.levels = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] # pre normalized
        
        self.normalized = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self.previous_msg_time = 0;
        self.previous_msg_time = 0;
        self.telemetry = []
        self.start_frame = 30
        self.cosmetic_frame = 0
        self.frame_number = self.start_frame
        self.coaster_status = "Waiting for coaster to complete initial run" 
        self.connection_status = "Not yet set"
       
        self.state_strings = ("Initializing", "Waiting", "Ready", "Running", "Completed")
        self.state = -1 # state not yet set
        self.is_paused = False

        self.rootTitle = "Space Coaster interface"
        
        self.actions = {'detected remote': self.detected_remote, 'activate': self.activate,
           'deactivate': self.deactivate, 'pause': self.pause, 'dispatch': self.dispatch,
           'reset': self.reset, 'emergency_stop': self.emergency_stop,
           'intensity' : self.set_intensity, 'info' : self.remote_info }
        if self.is_local_client:
           log.info("Starting as local client")
        else:
           self.SerialRemoteControl = SerialRemote(self.actions)
           self.UdpRemoteControl = UdpRemote(self.actions)


    def init_gui(self, frame):
        self.frame = frame
        self.ui = Ui_Frame()
        self.ui.setupUi(frame)

        # configure signals
        self.ui.btn_dispatch.clicked.connect(self.dispatch)
        self.ui.btn_pause.clicked.connect(self.pause)
        self.ui.btn_reset_rift.clicked.connect(self.reset)

        self.report_connection_status(self.connection_status, 'red')
        self.report_coaster_status(self.coaster_status, 'black')
        
        log.info("Client GUI initialized")

    def report_coaster_status(self, text, color):
        self.coaster_status_str = format("%s,%s" % (text,color))
        gutil.set_text(self.ui.lbl_coaster_status, text, color) 
    
    def report_connection_status(self, text, color):
        self.connection_status_str =  format("%s,%s" % (text,color))
        gutil.set_text(self.ui.lbl_coaster_connection, text, color) 
    
    def form_telemetry_msg(self):
        # state,frame,is_paused;x,y,z,r,p,y;coaster_state;connection_state
        xyzrpy = ",".join('%0.4f' % item for item in self.levels)
        self.telemetry_msg = format("%d,%d,%d;%s;%s;%s\n" % (self.state,self.cosmetic_frame,self.is_paused,
                             xyzrpy, self.coaster_status_str,self.connection_status_str))
        return self.telemetry_msg

    def detected_remote(self, info):
        if "Detected Remote" in info:
            gutil.set_text(self.ui.lbl_remote_status, info, "green")
        elif "Looking for Remote" in info:
            gutil.set_text(self.ui.lbl_remote_status, info, "orange")
        else:
             gutil.set_text(self.ui.lbl_remote_status, info, "red")
            
    def quit(self):
        self.command("quit")

    def activate(self):  #todo - move remote control response from clients to platform_controller if state can be managed
        self.command("enable")

    def deactivate(self):
        self.command("disable")

    def pause(self):
        if self.state == State.running:
            if self.is_paused: 
                log.debug("Unpausing coaster")
                self.set_focus("UnityWndClass") # or could use window title:'Coaster MSU'
                self.is_paused = False
            else:
                log.debug("Pausing coaster")
                self.set_focus("QWidget") 
                self.is_paused = True
                self.report_coaster_status("Coaster paused", "orange")
        else:
            self.command("swellForStairs")

    def reset(self):
        log.info("resetting Rift")
        self.right_mouse_click()

    def set_intensity(self, intensity_msg):
        self.command(intensity_msg)

    def emergency_stop(self):
        log.info("legacy emergency stop callback")
        self.deactivate()
 
    def command(self, cmd):
        if self.cmd_func is not None:
            log.debug("Requesting command: %s", cmd)
            self.cmd_func(cmd)
    
    def dispatch(self):
        log.debug('preparing to dispatch')
        self.command("ready")  # slow rise of platform
        self.command("unparkPlatform")
        #  self._sleep_func(1)
        self.left_mouse_click()
        log.debug("dispatched")
        self.frame_number = self.start_frame # start 1.5 seconds in

    def remote_info(self):
        log.debug("remote request for info")
        self.UdpRemoteControl.send("state," + self.state_strings[self.state])

    # def chair_status_changed(self, chair_status):
    #    log.debug(chair_status[0])
    
    def intensity_status_changed(self, intensity):
       gutil.set_text(self.ui.lbl_intensity_status, intensity[0], intensity[1])

    def begin(self, cmd_func, move_func, limits):
        self.cmd_func = cmd_func
        self.move_func = move_func
        self.limits = limits  # note limits are in mm and radians
        self.read_telemetry()
        self.xyzrpyQ = Queue()
        self.cmdQ = Queue()
        while True:
            try:
                log.debug("attempting to set focus")
                self.set_focus("UnityWndClass","Coaster MSU")
                log.info("found space coaster window")
                self.left_mouse_click()
                break
            except:
                reply =  QtGui.QMessageBox.question(self.frame, 'Coaster Connection Error!',
                        "Coaster not found, Start CoasterMSU and try again?" ,
                          QtGui.QMessageBox.Yes,  QtGui.QMessageBox.No)
                if reply == QtGui.QMessageBox.No:
                    raise ConnectionException("User aborted")
        log.info("Starting client listener thread")
        self.is_coaster_connected = -1
        t = Thread(target=self.listener_thread, args= (self.HOST, self.PORT))
        t.daemon = True
        t.start()
        
        self.report_connection_status("Connecting to Coaster", "orange") 
        while self.is_coaster_connected < 0:
            self.sleep_func(5)
            if self.is_coaster_connected != 1:
               log.warning("Coaster not connected - Is CoasterMSU running?")
               # QtGui.QMessageBox.warning( self.frame, 'Coaster Connection Error!',
               #                 "Coaster not Connected\nIs CoasterMSU running?" )
        if self.is_coaster_connected == 0:
            self.report_connection_status("Not connected to Coaster", "red") 
        else:
            self.report_connection_status("Space Coaster Connected", "green") 

    def fin(self):
        # client exit code goes here
        pass

    def get_current_pos(self):
        return self.levels

    def service(self):
        if not self.is_local_client:
            self.SerialRemoteControl.service()
            self.UdpRemoteControl.service()
        if self.is_coaster_connected == 0:
            self.report_connection_status("Not connected to Coaster", "red") 
        else:
            self.report_connection_status("Space Coaster Connected", "green") 
        msg = None
        try:
            if self.xyzrpyQ.qsize() == 0: 
                status = "Stopped at telemetry frame %d" % (self.frame_number - self.start_frame)
                self.report_coaster_status(status, "orange")
                if not self.is_paused:
                    log.warning("in service, setting is_paused to True because nothing in the coaster q")
                    self.is_paused = True
            else:
                if self.state == State.running and not self.is_paused:
                    try:
                        self.levels = self.telemetry[self.frame_number]
                    except IndexError:
                         log.warning("Invalid telemetry frame, reset frame to 0")
                         self.frame_number = 0
                    print "coaster running", self.frame_number, [ '%.2f' % elem for elem in self.levels]
                    if self.move_func:
                        self.move_func(self.levels)
                    cosmetic_frame = self.frame_number - self.start_frame
                    self.cosmetic_frame = cosmetic_frame 
                    if self.frame_number % 20 == 0:
                                if not self.is_local_client:
                                    self.UdpRemoteControl.send(format("time,%d,%d," % (cosmetic_frame/20, len(self.telemetry-self.start_frame)/20)))
                                status = format("Running frame %d, time %d" % (cosmetic_frame, cosmetic_frame/20))
                                self.report_coaster_status(status, "green") 
                    self.frame_number += 1
            
            while  self.cmdQ.qsize() > 0:
                state = self.cmdQ.get()
                self.process_state(state)
        except:  
            e = sys.exc_info()[0]
            s = traceback.format_exc()
            log.error("service error %s, %s, frame=%d", e, s, self.frame_number)

    def process_state(self, new_state):
        if self.state == new_state:  return
        if self.state == -1 and new_state == State.initializing:
            log.info("State transition to initial message from coaster")
            self.report_coaster_status("Starting software", "orange") 
        elif self.state == State.initializing and new_state == State.waiting:
            log.info("State transition from startup to waiting in lobby")
            self.report_coaster_status("Loading coaster", "orange") 
            self.sleep_func(2)
            self.left_mouse_click()
        elif self.state == State.waiting and new_state == State.ready:
            if not self.is_local_client:
                self.SerialRemoteControl.send(str(RideState.READY_FOR_DISPATCH))
                self.UdpRemoteControl.send("state," + "Ready for Dispatch")
            log.info("coaster is ready for dispatch")
            self.report_coaster_status("Ready for dispatch", "green")
        elif self.state == State.ready and new_state == State.running :
            self.activate()
            log.info("Coaster is starting run")
            self.report_coaster_status("Running", "Green")
            if not self.is_local_client:
                self.SerialRemoteControl.send(str(RideState.RUNNING))
                self.UdpRemoteControl.send("state," + "Running")
        elif self.state == State.running and new_state == State.completed:
            self.report_coaster_status("Entering hyperspace", "green")
            self.sleep_func(6)
            log.info("ready to reset")
            self.left_mouse_click()
            if not self.is_local_client:
                self.SerialRemoteControl.send(str(RideState.RESETTING))
                self.UdpRemoteControl.send("state," + "Resetting")
            self.deactivate()
        elif self.state == State.completed and new_state == State.waiting:
            log.info("State transition from completed to waiting in lobby")
            self.report_coaster_status("Getting ready", "orange")
            self.sleep_func(2)
            self.left_mouse_click()
        elif self.state == State.running and new_state == State.waiting:
            # this event happens if coaster sends running state after completed
            log.info("State transition from running to waiting in lobby")
            self.report_coaster_status("Waiting", "orange")
            self.sleep_func(2)
            self.left_mouse_click()
        elif self.state == State.completed and new_state == State.running:
            # anomaly to be ignored
            self.state = State.completed
        elif self.state == State.running and new_state == State.initializing:
            # this happens because of a brief running state after completion
            pass 
        else:
            log.warning("Ignoring out of sequence transition from state %s to %s", self.state_strings[self.state], self.state_strings[new_state])
            
        self.state = new_state 
        # self.report_coaster_status("Coaster state is: " + self.state_strings[self.state], "green")

    def listener_thread(self, HOST, PORT, ):
        try:
            self.MAX_MSG_LEN = 100
            client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            client.bind((HOST, PORT))
            log.info("opening space coaster socket on port %d", PORT)
        except:
            e = sys.exc_info()[0]
            s = traceback.format_exc()
            log.error("Space coaster connection thread init err %s,%s", e, s)
            self.is_coaster_connected = 0
        while True:
            try:
                msg = client.recv(self.MAX_MSG_LEN).rstrip()
                self.is_coaster_connected = 1
                if msg is not None:
                    # print msg
                    if msg.find("accel") == 0: 
                        msg = msg.replace(" ", "") # remove whitespace
                        accel = msg.split(',')
                        if not all(v == '0' for v in accel[1:7]): 
                            self.xyzrpyQ.put(accel[1:7])
                    elif msg.find("state") == 0:
                        s = msg.split(',')
                        self.cmdQ.put(int(s[1])) # state messages go onto command queue
                    elif "command" in msg:
                        #print msg
                        pass
            except:
                e = sys.exc_info()[0]
                s = traceback.format_exc()
                log.error("listener err %s,%s, msg(%s)", e, s, msg)
                self.is_coaster_connected = 0
                self.report_connection_status("Coaster connection error", "red") 

    def read_telemetry(self):
        try:
            path = os.path.abspath('space_coaster/chairGen_telemetry.csv')
            if not os.path.isfile(path): path = 'chairGen_telemetry.csv'
            with open(path, 'rb') as csvfile:
                log.info("opened space coaster telemetry file: chairGen_telemetry.csv")
                rows = csv.reader(csvfile, delimiter=',');
                for row in rows:
                    #  print row
                    if row is not None:
                        if len(row) >=6:
                            data = [float(f) for f in row[:6]]
                            # normalize
                            for idx, level in enumerate(data):
                                data[idx] = self.scale( data[idx], [-self.max_values[idx], self.max_values[idx], -1, 1] )
                            # print data
                            self.telemetry.append(data)
                log.info("Read %d frames into telemetry frame list",  (len(self.telemetry)))
                # following scales values to limits of configured platform 
                max = np.max(self.telemetry, axis = 0)
                min = np.min(self.telemetry, axis = 0)
                pos_factor = np.nan_to_num(self.limits/max)
                neg_factor = np.nan_to_num(self.limits/min)*-1
                #self.telemetry *= np.where(self.telemetry > 0, pos_factor,neg_factor)
                self.telemetry *= np.asarray([.7,.7,.7,.7,.7,.7])
                # print "new max", np.max(self.telemetry, axis = 0)
                # print "new min", np.min(self.telemetry, axis = 0)
                self.telemetry = np.asarray(self.telemetry, dtype=np.float32)
                # np.set_printoptions(precision=3,suppress=T
                # print self.telemetry
        except:
            e = sys.exc_info()[0]
            s = traceback.format_exc()
            log.error("Error reading telemetry file %s %s", e,s)
            
    #function to scale a value, range is a list containing: (from_min, from_max, to_min, to_max)   
    def scale(self, value, range):
        if value > range[1]:  # limit max
            return range[3]
        if value < range[0]:  # limit min
            return range[2]       
        if range[1] == range[0]:
            return range[2] #avoid div by zero error
        else:      
            return ( (value - range[0]) / (range[1] - range[0]) ) * (range[3] - range[2]) + range[2]


######### code for local client run from main ############

class LocalClient(QtGui.QMainWindow):
    """
    on state or status change local client will pass:
        current coaster state, current connection state, coaster status string, color
    every frame client will pass:
        frame number, xyzrpy
        
    commands:
        reset, dispatch, pause 
    
    """
    def __init__(self, sleep_func):
        log.info("Starting space coaster local client")
        try:
            QtGui.QMainWindow.__init__(self)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            
            self.client = InputInterface(sleep_func, True) 
            self.client.init_gui(self.ui.frame)
            limits = cfg.limits_1dof
            self.client.begin(self.cmd_func, self.move_func, limits)
            self.server = tcp_server.SockServer(port=10015)
            self.server.start()
            log.info("Started tcp server, this IP address is %s", self.server.get_local_ip())
            service_timer = QtCore.QTimer(self)
            service_timer.timeout.connect(self.service)
            log.info("Starting service timer")
            service_timer.start(50) 
        except:
            e = sys.exc_info()[0]  # report error
            s = traceback.format_exc()
            log.error("Space coaster local client %s %s", e, s)
 
    def service(self):
        self.client.service()
        self.server.send(self.client.form_telemetry_msg())
        self.server.service()
        if self.server.connected_clients() > 0:
            self.client.detected_remote("Detected Remote Client Connection")
        else:
             self.client.detected_remote("Remote client not Connected, this IP is: " + self.server.get_local_ip())
        while self.server.available():
            try:
                msg = self.server.receive()
                if msg:
                    event = msg.split("\n")
                    for e in event:
                        e = e.rstrip()
                        # print format("[%s], %d" % (e, len(e)))
                        if e in self.client.actions:
                            log.info("got remote client cmd %s", e)
                            self.client.actions[e]()
            except IndexError:
                log.warning("client queue index error")
        return True

    def cmd_func(self, cmd):  # command handler function called from Platform input
        if cmd == "quit": self.quit()

    def move_func(self, request):  # move handler to position platform as requested by Platform input
        pass
        
    def quit(self):
        log.info("Executing quit command")
        sys.exit()
 
if __name__ == "__main__":
    import gui_sleep
    from local_client_gui_defs import *
    import tcp_server
    sys.path.insert(0, '../output')
    import importlib  
    
    log_level = logging.INFO
    logging.basicConfig(level=log_level, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%H:%M:%S')

    # platform_selection = 'ConfigV3'
    platform_selection = 'configNextgen'
    cfg = importlib.import_module(platform_selection).PlatformConfig()

    gui_sleep._gui__app = QtGui.QApplication(sys.argv) 
    
    try:       
        local_client = LocalClient(gui_sleep.sleep )
        local_client.show()
        gui_sleep._gui__app.exec_()
    except ConnectionException as error:
        log.error("User aborted because space coaster not found") 
    except:
        e = sys.exc_info()[0]  # report error
        s = traceback.format_exc()
        log.error("space coaster main %s %s", e, s)
      
    gui_sleep._gui__app.exit()
    log.info("Exiting Platform Controller\n")
    