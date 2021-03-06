# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(509, 527)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 491, 711))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_4 = QtGui.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(10, 370, 465, 100))
        self.frame_4.setMinimumSize(QtCore.QSize(300, 100))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.btn_estop = QtGui.QPushButton(self.frame_4)
        self.btn_estop.setGeometry(QtCore.QRect(150, 30, 151, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_estop.setFont(font)
        self.btn_estop.setStyleSheet(_fromUtf8("QPushButton {\n"
"    color: yellow;\n"
"    border: 2px solid #555;\n"
"    border-radius: 20px;\n"
"    border-style: outset;\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #888,\n"
"        );\n"
"    padding: 5px;\n"
"    background-color: red;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
"        );\n"
"    background-color: red;\n"
"   color: white;\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"        radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
"        );\n"
"    }"))
        self.btn_estop.setObjectName(_fromUtf8("btn_estop"))
        self.tabWidget = QtGui.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 10, 491, 311))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tb_setup = QtGui.QWidget()
        self.tb_setup.setObjectName(_fromUtf8("tb_setup"))
        self.SerialGroupBox = QtGui.QGroupBox(self.tb_setup)
        self.SerialGroupBox.setGeometry(QtCore.QRect(30, 10, 371, 241))
        self.SerialGroupBox.setObjectName(_fromUtf8("SerialGroupBox"))
        self.btn_serial_connect = QtGui.QPushButton(self.SerialGroupBox)
        self.btn_serial_connect.setGeometry(QtCore.QRect(100, 200, 80, 23))
        self.btn_serial_connect.setMinimumSize(QtCore.QSize(80, 20))
        self.btn_serial_connect.setMaximumSize(QtCore.QSize(80, 16777215))
        self.btn_serial_connect.setStyleSheet(_fromUtf8(" background-color: silver;\n"
"color:black;"))
        self.btn_serial_connect.setObjectName(_fromUtf8("btn_serial_connect"))
        self.lbl_encoders = QtGui.QLabel(self.SerialGroupBox)
        self.lbl_encoders.setGeometry(QtCore.QRect(8, 35, 100, 16))
        self.lbl_encoders.setMinimumSize(QtCore.QSize(100, 0))
        self.lbl_encoders.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lbl_encoders.setObjectName(_fromUtf8("lbl_encoders"))
        self.cmb_encoder_port = QtGui.QComboBox(self.SerialGroupBox)
        self.cmb_encoder_port.setGeometry(QtCore.QRect(100, 37, 80, 20))
        self.cmb_encoder_port.setMinimumSize(QtCore.QSize(70, 20))
        self.cmb_encoder_port.setMaximumSize(QtCore.QSize(80, 16777215))
        self.cmb_encoder_port.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.cmb_encoder_port.setMinimumContentsLength(15)
        self.cmb_encoder_port.setObjectName(_fromUtf8("cmb_encoder_port"))
        self.lbl_imu = QtGui.QLabel(self.SerialGroupBox)
        self.lbl_imu.setGeometry(QtCore.QRect(8, 75, 100, 16))
        self.lbl_imu.setMinimumSize(QtCore.QSize(100, 0))
        self.lbl_imu.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lbl_imu.setObjectName(_fromUtf8("lbl_imu"))
        self.cmb_imu_port = QtGui.QComboBox(self.SerialGroupBox)
        self.cmb_imu_port.setGeometry(QtCore.QRect(100, 75, 80, 20))
        self.cmb_imu_port.setMinimumSize(QtCore.QSize(70, 20))
        self.cmb_imu_port.setMaximumSize(QtCore.QSize(80, 16777215))
        self.cmb_imu_port.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLength)
        self.cmb_imu_port.setMinimumContentsLength(15)
        self.cmb_imu_port.setObjectName(_fromUtf8("cmb_imu_port"))
        self.lbl_scale = QtGui.QLabel(self.SerialGroupBox)
        self.lbl_scale.setGeometry(QtCore.QRect(8, 116, 100, 16))
        self.lbl_scale.setMinimumSize(QtCore.QSize(100, 0))
        self.lbl_scale.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lbl_scale.setObjectName(_fromUtf8("lbl_scale"))
        self.cmb_scale_port = QtGui.QComboBox(self.SerialGroupBox)
        self.cmb_scale_port.setGeometry(QtCore.QRect(100, 116, 80, 20))
        self.cmb_scale_port.setMinimumSize(QtCore.QSize(70, 0))
        self.cmb_scale_port.setMaximumSize(QtCore.QSize(80, 16777215))
        self.cmb_scale_port.setObjectName(_fromUtf8("cmb_scale_port"))
        self.lbl_model = QtGui.QLabel(self.SerialGroupBox)
        self.lbl_model.setGeometry(QtCore.QRect(8, 155, 100, 16))
        self.lbl_model.setMinimumSize(QtCore.QSize(100, 0))
        self.lbl_model.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.lbl_model.setObjectName(_fromUtf8("lbl_model"))
        self.cmb_model_port = QtGui.QComboBox(self.SerialGroupBox)
        self.cmb_model_port.setGeometry(QtCore.QRect(100, 155, 80, 20))
        self.cmb_model_port.setMinimumSize(QtCore.QSize(70, 0))
        self.cmb_model_port.setMaximumSize(QtCore.QSize(80, 16777215))
        self.cmb_model_port.setObjectName(_fromUtf8("cmb_model_port"))
        self.chk_hold = QtGui.QCheckBox(self.SerialGroupBox)
        self.chk_hold.setGeometry(QtCore.QRect(298, 118, 44, 17))
        self.chk_hold.setObjectName(_fromUtf8("chk_hold"))
        self.chk_model_enabled = QtGui.QCheckBox(self.SerialGroupBox)
        self.chk_model_enabled.setGeometry(QtCore.QRect(200, 156, 70, 17))
        self.chk_model_enabled.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chk_model_enabled.setObjectName(_fromUtf8("chk_model_enabled"))
        self.label_20 = QtGui.QLabel(self.tb_setup)
        self.label_20.setGeometry(QtCore.QRect(226, 126, 39, 20))
        self.label_20.setMinimumSize(QtCore.QSize(0, 20))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.txt_weight_2 = QtGui.QLineEdit(self.tb_setup)
        self.txt_weight_2.setGeometry(QtCore.QRect(268, 126, 50, 20))
        self.txt_weight_2.setMinimumSize(QtCore.QSize(0, 20))
        self.txt_weight_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.txt_weight_2.setObjectName(_fromUtf8("txt_weight_2"))
        self.tabWidget.addTab(self.tb_setup, _fromUtf8(""))
        self.tb_calibrate = QtGui.QWidget()
        self.tb_calibrate.setObjectName(_fromUtf8("tb_calibrate"))
        self.PositionGroupBox = QtGui.QGroupBox(self.tb_calibrate)
        self.PositionGroupBox.setGeometry(QtCore.QRect(6, 230, 471, 51))
        self.PositionGroupBox.setMinimumSize(QtCore.QSize(400, 0))
        self.PositionGroupBox.setObjectName(_fromUtf8("PositionGroupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.PositionGroupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.txt_pos_0 = QtGui.QLineEdit(self.PositionGroupBox)
        self.txt_pos_0.setMinimumSize(QtCore.QSize(0, 20))
        self.txt_pos_0.setMaximumSize(QtCore.QSize(50, 16777215))
        self.txt_pos_0.setObjectName(_fromUtf8("txt_pos_0"))
        self.horizontalLayout.addWidget(self.txt_pos_0)
        self.txt_pos_1 = QtGui.QLineEdit(self.PositionGroupBox)
        self.txt_pos_1.setMinimumSize(QtCore.QSize(0, 20))
        self.txt_pos_1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.txt_pos_1.setObjectName(_fromUtf8("txt_pos_1"))
        self.horizontalLayout.addWidget(self.txt_pos_1)
        self.txt_pos_2 = QtGui.QLineEdit(self.PositionGroupBox)
        self.txt_pos_2.setMinimumSize(QtCore.QSize(0, 20))
        self.txt_pos_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.txt_pos_2.setObjectName(_fromUtf8("txt_pos_2"))
        self.horizontalLayout.addWidget(self.txt_pos_2)
        self.txt_pos_3 = QtGui.QLineEdit(self.PositionGroupBox)
        self.txt_pos_3.setMinimumSize(QtCore.QSize(0, 20))
        self.txt_pos_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.txt_pos_3.setObjectName(_fromUtf8("txt_pos_3"))
        self.horizontalLayout.addWidget(self.txt_pos_3)
        self.txt_pos_4 = QtGui.QLineEdit(self.PositionGroupBox)
        self.txt_pos_4.setMinimumSize(QtCore.QSize(0, 20))
        self.txt_pos_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.txt_pos_4.setObjectName(_fromUtf8("txt_pos_4"))
        self.horizontalLayout.addWidget(self.txt_pos_4)
        self.txt_pos_5 = QtGui.QLineEdit(self.PositionGroupBox)
        self.txt_pos_5.setMinimumSize(QtCore.QSize(0, 20))
        self.txt_pos_5.setMaximumSize(QtCore.QSize(50, 16777215))
        self.txt_pos_5.setObjectName(_fromUtf8("txt_pos_5"))
        self.horizontalLayout.addWidget(self.txt_pos_5)
        self.CalibrateGroupBox = QtGui.QGroupBox(self.tb_calibrate)
        self.CalibrateGroupBox.setGeometry(QtCore.QRect(10, 10, 471, 111))
        self.CalibrateGroupBox.setMinimumSize(QtCore.QSize(200, 0))
        self.CalibrateGroupBox.setObjectName(_fromUtf8("CalibrateGroupBox"))
        self.btn_calibrate = QtGui.QPushButton(self.CalibrateGroupBox)
        self.btn_calibrate.setGeometry(QtCore.QRect(12, 24, 75, 23))
        self.btn_calibrate.setObjectName(_fromUtf8("btn_calibrate"))
        self.label_7 = QtGui.QLabel(self.CalibrateGroupBox)
        self.label_7.setGeometry(QtCore.QRect(121, 28, 91, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.txt_steps = QtGui.QLineEdit(self.CalibrateGroupBox)
        self.txt_steps.setGeometry(QtCore.QRect(221, 25, 30, 20))
        self.txt_steps.setMaximumSize(QtCore.QSize(30, 16777215))
        self.txt_steps.setObjectName(_fromUtf8("txt_steps"))
        self.label_9 = QtGui.QLabel(self.CalibrateGroupBox)
        self.label_9.setGeometry(QtCore.QRect(277, 27, 51, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.txt_step_delay_ms = QtGui.QLineEdit(self.CalibrateGroupBox)
        self.txt_step_delay_ms.setGeometry(QtCore.QRect(330, 25, 40, 20))
        self.txt_step_delay_ms.setMinimumSize(QtCore.QSize(30, 0))
        self.txt_step_delay_ms.setMaximumSize(QtCore.QSize(40, 16777215))
        self.txt_step_delay_ms.setObjectName(_fromUtf8("txt_step_delay_ms"))
        self.label_8 = QtGui.QLabel(self.CalibrateGroupBox)
        self.label_8.setGeometry(QtCore.QRect(387, 26, 40, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.txt_repeats = QtGui.QLineEdit(self.CalibrateGroupBox)
        self.txt_repeats.setGeometry(QtCore.QRect(431, 25, 30, 20))
        self.txt_repeats.setMaximumSize(QtCore.QSize(30, 16777215))
        self.txt_repeats.setObjectName(_fromUtf8("txt_repeats"))
        self.txt_weight = QtGui.QLineEdit(self.CalibrateGroupBox)
        self.txt_weight.setGeometry(QtCore.QRect(58, 72, 50, 20))
        self.txt_weight.setMinimumSize(QtCore.QSize(0, 20))
        self.txt_weight.setMaximumSize(QtCore.QSize(50, 16777215))
        self.txt_weight.setObjectName(_fromUtf8("txt_weight"))
        self.label_10 = QtGui.QLabel(self.CalibrateGroupBox)
        self.label_10.setGeometry(QtCore.QRect(14, 73, 37, 20))
        self.label_10.setMinimumSize(QtCore.QSize(0, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.txt_p_to_d_fname = QtGui.QLineEdit(self.CalibrateGroupBox)
        self.txt_p_to_d_fname.setGeometry(QtCore.QRect(279, 72, 75, 20))
        self.txt_p_to_d_fname.setMinimumSize(QtCore.QSize(0, 20))
        self.txt_p_to_d_fname.setMaximumSize(QtCore.QSize(80, 16777215))
        self.txt_p_to_d_fname.setObjectName(_fromUtf8("txt_p_to_d_fname"))
        self.label_22 = QtGui.QLabel(self.CalibrateGroupBox)
        self.label_22.setGeometry(QtCore.QRect(132, 74, 141, 16))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.btn_save_step_data = QtGui.QPushButton(self.CalibrateGroupBox)
        self.btn_save_step_data.setGeometry(QtCore.QRect(370, 70, 75, 23))
        self.btn_save_step_data.setObjectName(_fromUtf8("btn_save_step_data"))
        self.label_7.raise_()
        self.label_8.raise_()
        self.btn_calibrate.raise_()
        self.txt_repeats.raise_()
        self.label_9.raise_()
        self.txt_steps.raise_()
        self.txt_step_delay_ms.raise_()
        self.txt_weight.raise_()
        self.label_10.raise_()
        self.txt_p_to_d_fname.raise_()
        self.label_22.raise_()
        self.btn_save_step_data.raise_()
        self.groupBox_4 = QtGui.QGroupBox(self.tb_calibrate)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 130, 471, 91))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.chk_combined_chart = QtGui.QCheckBox(self.groupBox_4)
        self.chk_combined_chart.setGeometry(QtCore.QRect(81, 59, 114, 17))
        self.chk_combined_chart.setChecked(True)
        self.chk_combined_chart.setObjectName(_fromUtf8("chk_combined_chart"))
        self.chk_individual_chart = QtGui.QCheckBox(self.groupBox_4)
        self.chk_individual_chart.setGeometry(QtCore.QRect(210, 59, 116, 17))
        self.chk_individual_chart.setChecked(True)
        self.chk_individual_chart.setObjectName(_fromUtf8("chk_individual_chart"))
        self.chk_std_dev = QtGui.QCheckBox(self.groupBox_4)
        self.chk_std_dev.setGeometry(QtCore.QRect(360, 59, 61, 17))
        self.chk_std_dev.setChecked(True)
        self.chk_std_dev.setObjectName(_fromUtf8("chk_std_dev"))
        self.label_17 = QtGui.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(10, 59, 61, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_19 = QtGui.QLabel(self.groupBox_4)
        self.label_19.setGeometry(QtCore.QRect(130, 21, 141, 20))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.txt_d_to_p_fname_2 = QtGui.QLineEdit(self.groupBox_4)
        self.txt_d_to_p_fname_2.setGeometry(QtCore.QRect(279, 22, 75, 20))
        self.txt_d_to_p_fname_2.setObjectName(_fromUtf8("txt_d_to_p_fname_2"))
        self.btn_create_d_to_p = QtGui.QPushButton(self.groupBox_4)
        self.btn_create_d_to_p.setGeometry(QtCore.QRect(370, 21, 75, 23))
        self.btn_create_d_to_p.setObjectName(_fromUtf8("btn_create_d_to_p"))
        self.tabWidget.addTab(self.tb_calibrate, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 10, 151, 251))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.lst_p_to_d = QtGui.QListWidget(self.groupBox_5)
        self.lst_p_to_d.setGeometry(QtCore.QRect(10, 20, 131, 192))
        self.lst_p_to_d.setObjectName(_fromUtf8("lst_p_to_d"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(200, 10, 151, 251))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.lst_d_to_p = QtGui.QListWidget(self.groupBox_6)
        self.lst_d_to_p.setGeometry(QtCore.QRect(10, 20, 131, 192))
        self.lst_d_to_p.setObjectName(_fromUtf8("lst_d_to_p"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_7.setGeometry(QtCore.QRect(360, 10, 111, 111))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.btn_merge_d_to_p = QtGui.QPushButton(self.groupBox_7)
        self.btn_merge_d_to_p.setGeometry(QtCore.QRect(20, 80, 75, 23))
        self.btn_merge_d_to_p.setObjectName(_fromUtf8("btn_merge_d_to_p"))
        self.label_18 = QtGui.QLabel(self.groupBox_7)
        self.label_18.setGeometry(QtCore.QRect(38, 53, 46, 13))
        self.label_18.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.txt_merged_d_to_p_fname = QtGui.QLineEdit(self.groupBox_7)
        self.txt_merged_d_to_p_fname.setGeometry(QtCore.QRect(6, 30, 101, 20))
        self.txt_merged_d_to_p_fname.setObjectName(_fromUtf8("txt_merged_d_to_p_fname"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(20, 110, 431, 161))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.btn_run_lookup = QtGui.QPushButton(self.groupBox)
        self.btn_run_lookup.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.btn_run_lookup.setObjectName(_fromUtf8("btn_run_lookup"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(20, 100, 61, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(20, 130, 71, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.txt_up_index = QtGui.QLineEdit(self.groupBox)
        self.txt_up_index.setGeometry(QtCore.QRect(100, 100, 91, 20))
        self.txt_up_index.setObjectName(_fromUtf8("txt_up_index"))
        self.txt_down_index = QtGui.QLineEdit(self.groupBox)
        self.txt_down_index.setGeometry(QtCore.QRect(100, 130, 91, 20))
        self.txt_down_index.setObjectName(_fromUtf8("txt_down_index"))
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(20, 30, 61, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.txt_up_pressure = QtGui.QLineEdit(self.groupBox)
        self.txt_up_pressure.setGeometry(QtCore.QRect(82, 30, 51, 20))
        self.txt_up_pressure.setObjectName(_fromUtf8("txt_up_pressure"))
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(157, 31, 71, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.txt_down_pressure = QtGui.QLineEdit(self.groupBox)
        self.txt_down_pressure.setGeometry(QtCore.QRect(238, 30, 51, 20))
        self.txt_down_pressure.setObjectName(_fromUtf8("txt_down_pressure"))
        self.label_15 = QtGui.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(328, 31, 21, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.txt_lookup_dur = QtGui.QLineEdit(self.groupBox)
        self.txt_lookup_dur.setGeometry(QtCore.QRect(356, 30, 51, 20))
        self.txt_lookup_dur.setObjectName(_fromUtf8("txt_lookup_dur"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 10, 231, 91))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.btn_load_d_to_p = QtGui.QPushButton(self.groupBox_2)
        self.btn_load_d_to_p.setGeometry(QtCore.QRect(30, 50, 71, 23))
        self.btn_load_d_to_p.setObjectName(_fromUtf8("btn_load_d_to_p"))
        self.txt_nbr_indices = QtGui.QLineEdit(self.groupBox_2)
        self.txt_nbr_indices.setGeometry(QtCore.QRect(170, 50, 41, 20))
        self.txt_nbr_indices.setObjectName(_fromUtf8("txt_nbr_indices"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(114, 52, 61, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.txt_d_to_p_fname = QtGui.QLineEdit(self.groupBox_2)
        self.txt_d_to_p_fname.setGeometry(QtCore.QRect(100, 20, 113, 20))
        self.txt_d_to_p_fname.setObjectName(_fromUtf8("txt_d_to_p_fname"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(270, 10, 181, 91))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.chk_delta_capture = QtGui.QCheckBox(self.groupBox_3)
        self.chk_delta_capture.setGeometry(QtCore.QRect(20, 54, 70, 17))
        self.chk_delta_capture.setObjectName(_fromUtf8("chk_delta_capture"))
        self.label_16 = QtGui.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(10, 20, 46, 13))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.txt_delta_fname = QtGui.QLineEdit(self.groupBox_3)
        self.txt_delta_fname.setGeometry(QtCore.QRect(52, 20, 121, 20))
        self.txt_delta_fname.setObjectName(_fromUtf8("txt_delta_fname"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tb_move = QtGui.QWidget()
        self.tb_move.setObjectName(_fromUtf8("tb_move"))
        self.MoveGroupBox = QtGui.QGroupBox(self.tb_move)
        self.MoveGroupBox.setGeometry(QtCore.QRect(10, 20, 465, 121))
        self.MoveGroupBox.setObjectName(_fromUtf8("MoveGroupBox"))
        self.frame_3 = QtGui.QFrame(self.MoveGroupBox)
        self.frame_3.setGeometry(QtCore.QRect(20, 17, 411, 41))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.rb_X = QtGui.QRadioButton(self.frame_3)
        self.rb_X.setGeometry(QtCore.QRect(11, 1, 60, 20))
        self.rb_X.setMinimumSize(QtCore.QSize(60, 20))
        self.rb_X.setMaximumSize(QtCore.QSize(60, 16777215))
        self.rb_X.setObjectName(_fromUtf8("rb_X"))
        self.rb_Y = QtGui.QRadioButton(self.frame_3)
        self.rb_Y.setGeometry(QtCore.QRect(77, 1, 60, 20))
        self.rb_Y.setMinimumSize(QtCore.QSize(60, 20))
        self.rb_Y.setMaximumSize(QtCore.QSize(60, 16777215))
        self.rb_Y.setObjectName(_fromUtf8("rb_Y"))
        self.rb_Z = QtGui.QRadioButton(self.frame_3)
        self.rb_Z.setGeometry(QtCore.QRect(143, 1, 60, 20))
        self.rb_Z.setMinimumSize(QtCore.QSize(60, 20))
        self.rb_Z.setMaximumSize(QtCore.QSize(60, 16777215))
        self.rb_Z.setChecked(True)
        self.rb_Z.setObjectName(_fromUtf8("rb_Z"))
        self.rb_Roll = QtGui.QRadioButton(self.frame_3)
        self.rb_Roll.setGeometry(QtCore.QRect(209, 1, 60, 20))
        self.rb_Roll.setMinimumSize(QtCore.QSize(60, 20))
        self.rb_Roll.setMaximumSize(QtCore.QSize(60, 16777215))
        self.rb_Roll.setObjectName(_fromUtf8("rb_Roll"))
        self.rb_Pitch = QtGui.QRadioButton(self.frame_3)
        self.rb_Pitch.setGeometry(QtCore.QRect(275, 1, 60, 20))
        self.rb_Pitch.setMinimumSize(QtCore.QSize(60, 20))
        self.rb_Pitch.setMaximumSize(QtCore.QSize(60, 16777215))
        self.rb_Pitch.setObjectName(_fromUtf8("rb_Pitch"))
        self.rb_Yaw = QtGui.QRadioButton(self.frame_3)
        self.rb_Yaw.setGeometry(QtCore.QRect(341, 1, 60, 20))
        self.rb_Yaw.setMinimumSize(QtCore.QSize(60, 20))
        self.rb_Yaw.setMaximumSize(QtCore.QSize(60, 16777215))
        self.rb_Yaw.setObjectName(_fromUtf8("rb_Yaw"))
        self.sld_percent = QtGui.QSlider(self.MoveGroupBox)
        self.sld_percent.setGeometry(QtCore.QRect(80, 58, 341, 22))
        self.sld_percent.setMinimum(-100)
        self.sld_percent.setMaximum(100)
        self.sld_percent.setProperty("value", 0)
        self.sld_percent.setOrientation(QtCore.Qt.Horizontal)
        self.sld_percent.setTickPosition(QtGui.QSlider.TicksBelow)
        self.sld_percent.setObjectName(_fromUtf8("sld_percent"))
        self.label_3 = QtGui.QLabel(self.MoveGroupBox)
        self.label_3.setGeometry(QtCore.QRect(228, 87, 46, 13))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(self.MoveGroupBox)
        self.label_5.setGeometry(QtCore.QRect(63, 87, 46, 13))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.MoveGroupBox)
        self.label_6.setGeometry(QtCore.QRect(393, 87, 46, 13))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label = QtGui.QLabel(self.MoveGroupBox)
        self.label.setGeometry(QtCore.QRect(228, 101, 46, 13))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.btn_move = QtGui.QPushButton(self.MoveGroupBox)
        self.btn_move.setGeometry(QtCore.QRect(18, 54, 41, 23))
        self.btn_move.setObjectName(_fromUtf8("btn_move"))
        self.RideGroupBox = QtGui.QGroupBox(self.tb_move)
        self.RideGroupBox.setGeometry(QtCore.QRect(10, 200, 471, 77))
        self.RideGroupBox.setObjectName(_fromUtf8("RideGroupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.RideGroupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btn_ride = QtGui.QPushButton(self.RideGroupBox)
        self.btn_ride.setMinimumSize(QtCore.QSize(0, 20))
        self.btn_ride.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btn_ride.setObjectName(_fromUtf8("btn_ride"))
        self.horizontalLayout_3.addWidget(self.btn_ride)
        self.cmb_ride = QtGui.QComboBox(self.RideGroupBox)
        self.cmb_ride.setMinimumSize(QtCore.QSize(100, 0))
        self.cmb_ride.setObjectName(_fromUtf8("cmb_ride"))
        self.horizontalLayout_3.addWidget(self.cmb_ride)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.lbl_ride_action = QtGui.QLabel(self.RideGroupBox)
        self.lbl_ride_action.setMinimumSize(QtCore.QSize(240, 20))
        self.lbl_ride_action.setMaximumSize(QtCore.QSize(140, 16777215))
        self.lbl_ride_action.setObjectName(_fromUtf8("lbl_ride_action"))
        self.horizontalLayout_3.addWidget(self.lbl_ride_action)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.DataGroupBox = QtGui.QGroupBox(self.tb_move)
        self.DataGroupBox.setGeometry(QtCore.QRect(10, 140, 475, 58))
        self.DataGroupBox.setObjectName(_fromUtf8("DataGroupBox"))
        self.btn_start_capture = QtGui.QPushButton(self.DataGroupBox)
        self.btn_start_capture.setGeometry(QtCore.QRect(11, 24, 60, 23))
        self.btn_start_capture.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btn_start_capture.setObjectName(_fromUtf8("btn_start_capture"))
        self.txt_weight_1 = QtGui.QLineEdit(self.DataGroupBox)
        self.txt_weight_1.setGeometry(QtCore.QRect(166, 25, 50, 20))
        self.txt_weight_1.setMinimumSize(QtCore.QSize(0, 20))
        self.txt_weight_1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.txt_weight_1.setObjectName(_fromUtf8("txt_weight_1"))
        self.label_21 = QtGui.QLabel(self.DataGroupBox)
        self.label_21.setGeometry(QtCore.QRect(123, 24, 37, 20))
        self.label_21.setMinimumSize(QtCore.QSize(0, 20))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.btn_save_raw = QtGui.QPushButton(self.DataGroupBox)
        self.btn_save_raw.setGeometry(QtCore.QRect(318, 24, 60, 23))
        self.btn_save_raw.setMinimumSize(QtCore.QSize(0, 20))
        self.btn_save_raw.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btn_save_raw.setObjectName(_fromUtf8("btn_save_raw"))
        self.txt_raw_data_fname = QtGui.QLineEdit(self.DataGroupBox)
        self.txt_raw_data_fname.setGeometry(QtCore.QRect(384, 25, 71, 20))
        self.txt_raw_data_fname.setMinimumSize(QtCore.QSize(0, 20))
        self.txt_raw_data_fname.setMaximumSize(QtCore.QSize(80, 16777215))
        self.txt_raw_data_fname.setObjectName(_fromUtf8("txt_raw_data_fname"))
        self.tabWidget.addTab(self.tb_move, _fromUtf8(""))
        self.ProgressGroupBox = QtGui.QGroupBox(self.frame)
        self.ProgressGroupBox.setGeometry(QtCore.QRect(0, 320, 491, 41))
        self.ProgressGroupBox.setObjectName(_fromUtf8("ProgressGroupBox"))
        self.progressBar = QtGui.QProgressBar(self.ProgressGroupBox)
        self.progressBar.setGeometry(QtCore.QRect(20, 15, 451, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Platform Test", None))
        self.btn_estop.setText(_translate("MainWindow", "Stop", None))
        self.SerialGroupBox.setTitle(_translate("MainWindow", "Comms", None))
        self.btn_serial_connect.setText(_translate("MainWindow", "    Connect    ", None))
        self.lbl_encoders.setText(_translate("MainWindow", "Encoders", None))
        self.lbl_imu.setText(_translate("MainWindow", "IMU", None))
        self.lbl_scale.setText(_translate("MainWindow", "Scale", None))
        self.lbl_model.setText(_translate("MainWindow", "Servo Model", None))
        self.chk_hold.setText(_translate("MainWindow", "Hold", None))
        self.chk_model_enabled.setText(_translate("MainWindow", "Enabled", None))
        self.label_20.setText(_translate("MainWindow", "Reading", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tb_setup), _translate("MainWindow", "Setup", None))
        self.PositionGroupBox.setTitle(_translate("MainWindow", "Encoder Readings", None))
        self.CalibrateGroupBox.setTitle(_translate("MainWindow", "Create Pressure to Distance file", None))
        self.btn_calibrate.setText(_translate("MainWindow", "Start", None))
        self.label_7.setText(_translate("MainWindow", "Nbr Pressure Steps", None))
        self.label_9.setText(_translate("MainWindow", "Delay (ms)", None))
        self.label_8.setText(_translate("MainWindow", "Repeats", None))
        self.label_10.setText(_translate("MainWindow", "Load kg", None))
        self.label_22.setText(_translate("MainWindow", "Pressure to distance filename", None))
        self.btn_save_step_data.setText(_translate("MainWindow", "Save", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Create Distance to Pressure file", None))
        self.chk_combined_chart.setText(_translate("MainWindow", "Combined readings", None))
        self.chk_individual_chart.setText(_translate("MainWindow", " Individual readings", None))
        self.chk_std_dev.setText(_translate("MainWindow", "Std Dev", None))
        self.label_17.setText(_translate("MainWindow", "Show Charts", None))
        self.label_19.setText(_translate("MainWindow", "Distance to pressure filename", None))
        self.btn_create_d_to_p.setText(_translate("MainWindow", "Process", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tb_calibrate), _translate("MainWindow", "Calibrate", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Pressure to Distance files", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Distance to Pressure files", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "Merge D to P profiles", None))
        self.btn_merge_d_to_p.setText(_translate("MainWindow", "Merge", None))
        self.label_18.setText(_translate("MainWindow", "File path", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Data", None))
        self.groupBox.setTitle(_translate("MainWindow", "Select up and down profiles closest to current load", None))
        self.btn_run_lookup.setText(_translate("MainWindow", "Run", None))
        self.label_11.setText(_translate("MainWindow", "Up Indices", None))
        self.label_12.setText(_translate("MainWindow", "Down Indices", None))
        self.label_13.setText(_translate("MainWindow", "Up Pressure", None))
        self.label_14.setText(_translate("MainWindow", "Down Pressure", None))
        self.label_15.setText(_translate("MainWindow", "Dur", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Load Distance to Pressure Profiles", None))
        self.btn_load_d_to_p.setText(_translate("MainWindow", "Load", None))
        self.label_4.setText(_translate("MainWindow", "Nbr Indices", None))
        self.label_2.setText(_translate("MainWindow", "D-to-P filename", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Capture Distance Deltas", None))
        self.chk_delta_capture.setText(_translate("MainWindow", "Capture", None))
        self.label_16.setText(_translate("MainWindow", "Fname", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Profiles", None))
        self.MoveGroupBox.setTitle(_translate("MainWindow", "Movement", None))
        self.rb_X.setText(_translate("MainWindow", "X", None))
        self.rb_Y.setText(_translate("MainWindow", "Y", None))
        self.rb_Z.setText(_translate("MainWindow", "Z", None))
        self.rb_Roll.setText(_translate("MainWindow", "Roll", None))
        self.rb_Pitch.setText(_translate("MainWindow", "Pitch", None))
        self.rb_Yaw.setText(_translate("MainWindow", "Yaw", None))
        self.label_3.setText(_translate("MainWindow", "0", None))
        self.label_5.setText(_translate("MainWindow", "-100", None))
        self.label_6.setText(_translate("MainWindow", "100", None))
        self.label.setText(_translate("MainWindow", "Percent", None))
        self.btn_move.setText(_translate("MainWindow", "Move", None))
        self.RideGroupBox.setTitle(_translate("MainWindow", "Ride Control", None))
        self.btn_ride.setText(_translate("MainWindow", "Start", None))
        self.lbl_ride_action.setText(_translate("MainWindow", "Ride Not Active", None))
        self.DataGroupBox.setTitle(_translate("MainWindow", "Data  Capture", None))
        self.btn_start_capture.setText(_translate("MainWindow", "Capture", None))
        self.label_21.setText(_translate("MainWindow", "Load kg", None))
        self.btn_save_raw.setText(_translate("MainWindow", "Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tb_move), _translate("MainWindow", "Move", None))
        self.ProgressGroupBox.setTitle(_translate("MainWindow", "Progress", None))

