from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
from PyQt6.QtCore import QFile, QIODevice, QTextStream, QCoreApplication   
from PyQt6.QtGui import QIcon

from UI.calendar_ui import Ui_MainWindow


class Calendar(QMainWindow, Ui_MainWindow):
    def __init__(self, home_window: object):
        super().__init__(home_window)
        # Save the home window reference
        self.home_window = home_window

        # Load the UI file
        self.setupUi(self)
        self.initUI()
        # Load the QSS style sheet
        style_sheet_file = QFile("calendar.qss")
        if style_sheet_file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):
            style_sheet = QTextStream(style_sheet_file).readAll()
            self.setStyleSheet(style_sheet)
        
    def initUI(self):
        # Set button icon
        self.btn_home.setIcon(QIcon("items\icons\home.png"))

        self.btn_home.pressed.connect(self.to_home)
    
    def to_home(self):
        # Close the current window
        self.hide()
        # Open the main window here
        self.home_window.show()

    # If this window closed quit app
    def closeEvent(self, event):
        QCoreApplication.quit()
        event.accept()