# Form implementation generated from reading ui file 'calendar.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendar = QtWidgets.QCalendarWidget(parent=self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(50, 0, 491, 501))
        self.calendar.setObjectName("calendar")
        self.btn_add_event = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_add_event.setGeometry(QtCore.QRect(50, 510, 491, 51))
        self.btn_add_event.setObjectName("btn_add_event")
        self.events = QtWidgets.QListWidget(parent=self.centralwidget)
        self.events.setGeometry(QtCore.QRect(550, 2, 441, 501))
        self.events.setObjectName("events")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(550, 510, 441, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_info = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_info.setEnabled(False)
        self.btn_info.setObjectName("btn_info")
        self.horizontalLayout.addWidget(self.btn_info)
        self.btn_delete = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_delete.setEnabled(False)
        self.btn_delete.setObjectName("btn_delete")
        self.horizontalLayout.addWidget(self.btn_delete)
        self.btn_back = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(5, 0, 41, 41))
        self.btn_back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../items/icons/back_arrow.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_back.setIcon(icon)
        self.btn_back.setObjectName("btn_back")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_add_event.setText(_translate("MainWindow", "Добавить"))
        self.btn_info.setText(_translate("MainWindow", "Информация"))
        self.btn_delete.setText(_translate("MainWindow", "Удалить"))
