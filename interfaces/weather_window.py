from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
from PyQt6.QtCore import QFile, QIODevice, QTextStream


class Weather(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI file
        uic.loadUi('UI/weather.ui', self)
        # Load the QSS style sheet
        style_sheet_file = QFile("style.qss")
        if style_sheet_file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):
            style_sheet = QTextStream(style_sheet_file).readAll()
            self.setStyleSheet(style_sheet)
        self.initUI()
    
    def initUI(self):
        pass