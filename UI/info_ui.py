# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 250)
        Dialog.setMinimumSize(QtCore.QSize(400, 250))
        Dialog.setMaximumSize(QtCore.QSize(400, 250))
        Dialog.setAutoFillBackground(False)
        self.frame = QtWidgets.QFrame(parent=Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.frame.setMinimumSize(QtCore.QSize(401, 301))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setContentsMargins(2, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 87 10pt \"Segoe UI Black\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.event_edit = QtWidgets.QLineEdit(parent=self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.event_edit.setFont(font)
        self.event_edit.setStyleSheet("border-radius: 8px;\n"
"font: 87 10pt \"Segoe UI Black\";")
        self.event_edit.setMaxLength(60)
        self.event_edit.setObjectName("event_edit")
        self.horizontalLayout.addWidget(self.event_edit)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_7 = QtWidgets.QFrame(parent=self.frame_5)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_9 = QtWidgets.QFrame(parent=self.frame_7)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 87 10pt \"Segoe UI Black\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.dateEdit = QtWidgets.QDateEdit(parent=self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("border-radius: 8px;\n"
"font: 87 10pt \"Segoe UI Black\";")
        self.dateEdit.setObjectName("dateEdit")
        self.verticalLayout_4.addWidget(self.dateEdit)
        self.horizontalLayout_2.addWidget(self.frame_9)
        self.frame_8 = QtWidgets.QFrame(parent=self.frame_7)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_2.addWidget(self.frame_8)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.frame_6 = QtWidgets.QFrame(parent=self.frame_5)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_10 = QtWidgets.QFrame(parent=self.frame_6)
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_10)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font: 87 10pt \"Segoe UI Black\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.timeEdit = QtWidgets.QTimeEdit(parent=self.frame_10)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.timeEdit.setFont(font)
        self.timeEdit.setStyleSheet("border-radius: 8px;\n"
"font: 87 10pt \"Segoe UI Black\";")
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout_5.addWidget(self.timeEdit)
        self.horizontalLayout_3.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(parent=self.frame_6)
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_3.addWidget(self.frame_11)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 87 11pt \"Segoe UI Black\";")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_12 = QtWidgets.QFrame(parent=self.frame)
        self.frame_12.setStyleSheet("font: 87 8pt \"Segoe UI Black\";")
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_save = QtWidgets.QPushButton(parent=self.frame_12)
        self.btn_save.setMinimumSize(QtCore.QSize(0, 20))
        self.btn_save.setStyleSheet("background: rgb(115, 115, 173);\\n\n"
"border: None;\n"
"border-radius: 6px;\n"
"")
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_5.addWidget(self.btn_save)
        self.btn_cancel = QtWidgets.QPushButton(parent=self.frame_12)
        self.btn_cancel.setMinimumSize(QtCore.QSize(0, 20))
        self.btn_cancel.setStyleSheet("background: rgb(115, 115, 173);\\n\n"
"border: None;\n"
"border-radius: 6px;\n"
"")
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_5.addWidget(self.btn_cancel)
        self.verticalLayout.addWidget(self.frame_12, 0, QtCore.Qt.AlignmentFlag.AlignTop)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Information"))
        self.label.setText(_translate("Dialog", "Event name:"))
        self.label_2.setText(_translate("Dialog", "Event date:"))
        self.label_3.setText(_translate("Dialog", "Event time:"))
        self.label_4.setText(_translate("Dialog", "You can change info about this event if you want"))
        self.btn_save.setText(_translate("Dialog", "Save"))
        self.btn_cancel.setText(_translate("Dialog", "Cancel"))
