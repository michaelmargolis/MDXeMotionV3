# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'output_gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(800, 440)
        Frame.setStyleSheet("")
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_output = QtWidgets.QFrame(Frame)
        self.frm_output.setGeometry(QtCore.QRect(0, 0, 791, 351))
        self.frm_output.setStyleSheet("background-color: #f0f0f0")
        self.frm_output.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_output.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_output.setObjectName("frm_output")
        self.gb_actuator_percent = QtWidgets.QGroupBox(self.frm_output)
        self.gb_actuator_percent.setGeometry(QtCore.QRect(410, 10, 371, 161))
        self.gb_actuator_percent.setObjectName("gb_actuator_percent")
        self.muscle_3 = QtWidgets.QFrame(self.gb_actuator_percent)
        self.muscle_3.setEnabled(False)
        self.muscle_3.setGeometry(QtCore.QRect(40, 90, 200, 16))
        self.muscle_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.muscle_3.setLineWidth(8)
        self.muscle_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.muscle_3.setObjectName("muscle_3")
        self.muscle_4 = QtWidgets.QFrame(self.gb_actuator_percent)
        self.muscle_4.setEnabled(False)
        self.muscle_4.setGeometry(QtCore.QRect(40, 110, 200, 16))
        self.muscle_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.muscle_4.setLineWidth(8)
        self.muscle_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.muscle_4.setObjectName("muscle_4")
        self.muscle_5 = QtWidgets.QFrame(self.gb_actuator_percent)
        self.muscle_5.setEnabled(False)
        self.muscle_5.setGeometry(QtCore.QRect(40, 130, 200, 16))
        self.muscle_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.muscle_5.setLineWidth(8)
        self.muscle_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.muscle_5.setObjectName("muscle_5")
        self.muscle_2 = QtWidgets.QFrame(self.gb_actuator_percent)
        self.muscle_2.setEnabled(False)
        self.muscle_2.setGeometry(QtCore.QRect(40, 70, 200, 16))
        self.muscle_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.muscle_2.setLineWidth(8)
        self.muscle_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.muscle_2.setObjectName("muscle_2")
        self.muscle_1 = QtWidgets.QFrame(self.gb_actuator_percent)
        self.muscle_1.setEnabled(False)
        self.muscle_1.setGeometry(QtCore.QRect(40, 50, 200, 16))
        self.muscle_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.muscle_1.setLineWidth(8)
        self.muscle_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.muscle_1.setObjectName("muscle_1")
        self.muscle_0 = QtWidgets.QFrame(self.gb_actuator_percent)
        self.muscle_0.setEnabled(False)
        self.muscle_0.setGeometry(QtCore.QRect(40, 30, 200, 16))
        self.muscle_0.setFrameShadow(QtWidgets.QFrame.Plain)
        self.muscle_0.setLineWidth(8)
        self.muscle_0.setFrameShape(QtWidgets.QFrame.HLine)
        self.muscle_0.setObjectName("muscle_0")
        self.txt_muscle_0 = QtWidgets.QLabel(self.gb_actuator_percent)
        self.txt_muscle_0.setGeometry(QtCore.QRect(260, 30, 71, 16))
        self.txt_muscle_0.setObjectName("txt_muscle_0")
        self.txt_muscle_1 = QtWidgets.QLabel(self.gb_actuator_percent)
        self.txt_muscle_1.setGeometry(QtCore.QRect(260, 50, 71, 16))
        self.txt_muscle_1.setObjectName("txt_muscle_1")
        self.txt_muscle_2 = QtWidgets.QLabel(self.gb_actuator_percent)
        self.txt_muscle_2.setGeometry(QtCore.QRect(260, 70, 71, 16))
        self.txt_muscle_2.setObjectName("txt_muscle_2")
        self.txt_muscle_3 = QtWidgets.QLabel(self.gb_actuator_percent)
        self.txt_muscle_3.setGeometry(QtCore.QRect(260, 90, 71, 16))
        self.txt_muscle_3.setObjectName("txt_muscle_3")
        self.txt_muscle_4 = QtWidgets.QLabel(self.gb_actuator_percent)
        self.txt_muscle_4.setGeometry(QtCore.QRect(260, 110, 71, 16))
        self.txt_muscle_4.setObjectName("txt_muscle_4")
        self.txt_muscle_5 = QtWidgets.QLabel(self.gb_actuator_percent)
        self.txt_muscle_5.setGeometry(QtCore.QRect(260, 130, 71, 16))
        self.txt_muscle_5.setObjectName("txt_muscle_5")
        self.grp_request = QtWidgets.QGroupBox(self.frm_output)
        self.grp_request.setGeometry(QtCore.QRect(40, 10, 141, 331))
        self.grp_request.setObjectName("grp_request")
        self.txt_xform_0 = QtWidgets.QLineEdit(self.grp_request)
        self.txt_xform_0.setGeometry(QtCore.QRect(60, 40, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.txt_xform_0.setFont(font)
        self.txt_xform_0.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_xform_0.setObjectName("txt_xform_0")
        self.txt_xform_3 = QtWidgets.QLineEdit(self.grp_request)
        self.txt_xform_3.setGeometry(QtCore.QRect(60, 130, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.txt_xform_3.setFont(font)
        self.txt_xform_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_xform_3.setObjectName("txt_xform_3")
        self.txt_xform_1 = QtWidgets.QLineEdit(self.grp_request)
        self.txt_xform_1.setGeometry(QtCore.QRect(60, 70, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.txt_xform_1.setFont(font)
        self.txt_xform_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_xform_1.setObjectName("txt_xform_1")
        self.txt_xform_2 = QtWidgets.QLineEdit(self.grp_request)
        self.txt_xform_2.setGeometry(QtCore.QRect(60, 100, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.txt_xform_2.setFont(font)
        self.txt_xform_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_xform_2.setObjectName("txt_xform_2")
        self.txt_xform_4 = QtWidgets.QLineEdit(self.grp_request)
        self.txt_xform_4.setGeometry(QtCore.QRect(60, 160, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.txt_xform_4.setFont(font)
        self.txt_xform_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_xform_4.setObjectName("txt_xform_4")
        self.txt_xform_5 = QtWidgets.QLineEdit(self.grp_request)
        self.txt_xform_5.setGeometry(QtCore.QRect(60, 190, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.txt_xform_5.setFont(font)
        self.txt_xform_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_xform_5.setObjectName("txt_xform_5")
        self.label_3 = QtWidgets.QLabel(self.grp_request)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 41, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.grp_request)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 41, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.grp_request)
        self.label_5.setGeometry(QtCore.QRect(10, 190, 41, 16))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.grp_request)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 41, 16))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.grp_request)
        self.label_7.setGeometry(QtCore.QRect(10, 40, 41, 16))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.grp_request)
        self.label_8.setGeometry(QtCore.QRect(10, 70, 41, 16))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gb_processing_dur = QtWidgets.QGroupBox(self.frm_output)
        self.gb_processing_dur.setGeometry(QtCore.QRect(410, 272, 371, 71))
        self.gb_processing_dur.setObjectName("gb_processing_dur")
        self.txt_processing_dur = QtWidgets.QLabel(self.gb_processing_dur)
        self.txt_processing_dur.setGeometry(QtCore.QRect(260, 30, 71, 16))
        self.txt_processing_dur.setObjectName("txt_processing_dur")
        self.line = QtWidgets.QFrame(self.gb_processing_dur)
        self.line.setGeometry(QtCore.QRect(132, 24, 16, 21))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.rect_dur = QtWidgets.QFrame(self.gb_processing_dur)
        self.rect_dur.setEnabled(False)
        self.rect_dur.setGeometry(QtCore.QRect(40, 33, 200, 10))
        self.rect_dur.setStyleSheet("color: rgb(85, 255, 127);")
        self.rect_dur.setFrameShadow(QtWidgets.QFrame.Plain)
        self.rect_dur.setLineWidth(8)
        self.rect_dur.setFrameShape(QtWidgets.QFrame.HLine)
        self.rect_dur.setObjectName("rect_dur")
        self.label_9 = QtWidgets.QLabel(self.gb_processing_dur)
        self.label_9.setGeometry(QtCore.QRect(130, 45, 46, 13))
        self.label_9.setObjectName("label_9")
        self.bg_load_indices = QtWidgets.QGroupBox(self.frm_output)
        self.bg_load_indices.setGeometry(QtCore.QRect(411, 170, 371, 98))
        self.bg_load_indices.setObjectName("bg_load_indices")
        self.label_10 = QtWidgets.QLabel(self.bg_load_indices)
        self.label_10.setGeometry(QtCore.QRect(52, 24, 21, 16))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.txt_up_idx_0 = QtWidgets.QLineEdit(self.bg_load_indices)
        self.txt_up_idx_0.setGeometry(QtCore.QRect(50, 44, 31, 20))
        self.txt_up_idx_0.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_up_idx_0.setObjectName("txt_up_idx_0")
        self.txt_up_idx_1 = QtWidgets.QLineEdit(self.bg_load_indices)
        self.txt_up_idx_1.setGeometry(QtCore.QRect(88, 44, 31, 20))
        self.txt_up_idx_1.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_up_idx_1.setObjectName("txt_up_idx_1")
        self.label_11 = QtWidgets.QLabel(self.bg_load_indices)
        self.label_11.setGeometry(QtCore.QRect(90, 24, 21, 16))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.txt_up_idx_2 = QtWidgets.QLineEdit(self.bg_load_indices)
        self.txt_up_idx_2.setGeometry(QtCore.QRect(126, 44, 31, 20))
        self.txt_up_idx_2.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_up_idx_2.setObjectName("txt_up_idx_2")
        self.txt_up_idx_3 = QtWidgets.QLineEdit(self.bg_load_indices)
        self.txt_up_idx_3.setGeometry(QtCore.QRect(164, 44, 31, 20))
        self.txt_up_idx_3.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_up_idx_3.setObjectName("txt_up_idx_3")
        self.label_12 = QtWidgets.QLabel(self.bg_load_indices)
        self.label_12.setGeometry(QtCore.QRect(131, 24, 21, 16))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.bg_load_indices)
        self.label_13.setGeometry(QtCore.QRect(170, 24, 21, 16))
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.txt_up_idx_4 = QtWidgets.QLineEdit(self.bg_load_indices)
        self.txt_up_idx_4.setGeometry(QtCore.QRect(201, 44, 31, 20))
        self.txt_up_idx_4.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_up_idx_4.setObjectName("txt_up_idx_4")
        self.txt_up_idx_5 = QtWidgets.QLineEdit(self.bg_load_indices)
        self.txt_up_idx_5.setGeometry(QtCore.QRect(239, 44, 31, 20))
        self.txt_up_idx_5.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_up_idx_5.setObjectName("txt_up_idx_5")
        self.label_14 = QtWidgets.QLabel(self.bg_load_indices)
        self.label_14.setGeometry(QtCore.QRect(206, 24, 21, 16))
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.bg_load_indices)
        self.label_15.setGeometry(QtCore.QRect(243, 24, 21, 16))
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.txt_down_idx_4 = QtWidgets.QLineEdit(self.bg_load_indices)
        self.txt_down_idx_4.setGeometry(QtCore.QRect(201, 69, 31, 20))
        self.txt_down_idx_4.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_down_idx_4.setObjectName("txt_down_idx_4")
        self.txt_down_idx_2 = QtWidgets.QLineEdit(self.bg_load_indices)
        self.txt_down_idx_2.setGeometry(QtCore.QRect(126, 69, 31, 20))
        self.txt_down_idx_2.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_down_idx_2.setObjectName("txt_down_idx_2")
        self.txt_down_idx_0 = QtWidgets.QLineEdit(self.bg_load_indices)
        self.txt_down_idx_0.setGeometry(QtCore.QRect(50, 69, 31, 20))
        self.txt_down_idx_0.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_down_idx_0.setObjectName("txt_down_idx_0")
        self.txt_down_idx_5 = QtWidgets.QLineEdit(self.bg_load_indices)
        self.txt_down_idx_5.setGeometry(QtCore.QRect(239, 69, 31, 20))
        self.txt_down_idx_5.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_down_idx_5.setObjectName("txt_down_idx_5")
        self.txt_down_idx_3 = QtWidgets.QLineEdit(self.bg_load_indices)
        self.txt_down_idx_3.setGeometry(QtCore.QRect(164, 69, 31, 20))
        self.txt_down_idx_3.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_down_idx_3.setObjectName("txt_down_idx_3")
        self.txt_down_idx_1 = QtWidgets.QLineEdit(self.bg_load_indices)
        self.txt_down_idx_1.setGeometry(QtCore.QRect(88, 69, 31, 20))
        self.txt_down_idx_1.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_down_idx_1.setObjectName("txt_down_idx_1")
        self.rb_manual = QtWidgets.QRadioButton(self.bg_load_indices)
        self.rb_manual.setGeometry(QtCore.QRect(280, 30, 81, 17))
        self.rb_manual.setObjectName("rb_manual")
        self.rb_encoders = QtWidgets.QRadioButton(self.bg_load_indices)
        self.rb_encoders.setGeometry(QtCore.QRect(280, 60, 81, 17))
        self.rb_encoders.setChecked(True)
        self.rb_encoders.setObjectName("rb_encoders")
        self.label_16 = QtWidgets.QLabel(self.bg_load_indices)
        self.label_16.setGeometry(QtCore.QRect(10, 46, 31, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.bg_load_indices)
        self.label_17.setGeometry(QtCore.QRect(9, 71, 41, 16))
        self.label_17.setObjectName("label_17")
        self.frame = QtWidgets.QFrame(self.frm_output)
        self.frame.setGeometry(QtCore.QRect(208, 16, 181, 325))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.line_10 = QtWidgets.QFrame(self.frame)
        self.line_10.setGeometry(QtCore.QRect(30, 64, 118, 3))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.frame)
        self.line_11.setGeometry(QtCore.QRect(85, 0, 20, 321))
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.frame)
        self.line_12.setGeometry(QtCore.QRect(36, 164, 118, 3))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.frame)
        self.line_13.setGeometry(QtCore.QRect(40, 263, 118, 3))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.lbl_front_view = QtWidgets.QLabel(self.frame)
        self.lbl_front_view.setGeometry(QtCore.QRect(49, 20, 90, 90))
        self.lbl_front_view.setText("")
        self.lbl_front_view.setPixmap(QtGui.QPixmap("images/front.png"))
        self.lbl_front_view.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_front_view.setObjectName("lbl_front_view")
        self.lbl_top_view = QtWidgets.QLabel(self.frm_output)
        self.lbl_top_view.setGeometry(QtCore.QRect(258, 236, 90, 90))
        self.lbl_top_view.setText("")
        self.lbl_top_view.setPixmap(QtGui.QPixmap("images/top.png"))
        self.lbl_top_view.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_top_view.setObjectName("lbl_top_view")
        self.lbl_side_view = QtWidgets.QLabel(self.frm_output)
        self.lbl_side_view.setGeometry(QtCore.QRect(258, 136, 90, 90))
        self.lbl_side_view.setText("")
        self.lbl_side_view.setPixmap(QtGui.QPixmap("images/side.png"))
        self.lbl_side_view.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_side_view.setObjectName("lbl_side_view")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.gb_actuator_percent.setTitle(_translate("Frame", "Actuators"))
        self.txt_muscle_0.setText(_translate("Frame", "Muscle 0"))
        self.txt_muscle_1.setText(_translate("Frame", "Muscle 1"))
        self.txt_muscle_2.setText(_translate("Frame", "Muscle 2"))
        self.txt_muscle_3.setText(_translate("Frame", "Muscle 3"))
        self.txt_muscle_4.setText(_translate("Frame", "Muscle 4"))
        self.txt_muscle_5.setText(_translate("Frame", "Muscle 5"))
        self.grp_request.setTitle(_translate("Frame", "Request Transform"))
        self.txt_xform_0.setText(_translate("Frame", "000"))
        self.txt_xform_3.setText(_translate("Frame", "0.00"))
        self.txt_xform_1.setText(_translate("Frame", "000"))
        self.txt_xform_2.setText(_translate("Frame", "000"))
        self.txt_xform_4.setText(_translate("Frame", "0.00"))
        self.txt_xform_5.setText(_translate("Frame", "0.00"))
        self.label_3.setText(_translate("Frame", "Roll"))
        self.label_4.setText(_translate("Frame", "Pitch"))
        self.label_5.setText(_translate("Frame", "Yaw"))
        self.label_6.setText(_translate("Frame", "Z"))
        self.label_7.setText(_translate("Frame", "X"))
        self.label_8.setText(_translate("Frame", "Y"))
        self.gb_processing_dur.setTitle(_translate("Frame", "Processing duration "))
        self.txt_processing_dur.setText(_translate("Frame", "0"))
        self.label_9.setText(_translate("Frame", "10 ms"))
        self.bg_load_indices.setTitle(_translate("Frame", "Loaded Indices"))
        self.label_10.setText(_translate("Frame", "0"))
        self.txt_up_idx_0.setText(_translate("Frame", "0.0"))
        self.txt_up_idx_1.setText(_translate("Frame", "0.0"))
        self.label_11.setText(_translate("Frame", "1"))
        self.txt_up_idx_2.setText(_translate("Frame", "0.0"))
        self.txt_up_idx_3.setText(_translate("Frame", "0.0"))
        self.label_12.setText(_translate("Frame", "2"))
        self.label_13.setText(_translate("Frame", "3"))
        self.txt_up_idx_4.setText(_translate("Frame", "0.0"))
        self.txt_up_idx_5.setText(_translate("Frame", "0.0"))
        self.label_14.setText(_translate("Frame", "4"))
        self.label_15.setText(_translate("Frame", "5"))
        self.txt_down_idx_4.setText(_translate("Frame", "0.0"))
        self.txt_down_idx_2.setText(_translate("Frame", "0.0"))
        self.txt_down_idx_0.setText(_translate("Frame", "0.0"))
        self.txt_down_idx_5.setText(_translate("Frame", "0.0"))
        self.txt_down_idx_3.setText(_translate("Frame", "0.0"))
        self.txt_down_idx_1.setText(_translate("Frame", "0.0"))
        self.rb_manual.setText(_translate("Frame", "Manual"))
        self.rb_encoders.setText(_translate("Frame", "Encoders"))
        self.label_16.setText(_translate("Frame", "Up"))
        self.label_17.setText(_translate("Frame", "Down"))

