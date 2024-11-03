from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
from PyQt6.QtCore import QFile, QIODevice, QTextStream

from calendar import Calendar
from weather_window import Weather

#TODO Разобраться с импортом из ui/main.py, питон не видит папку ui
#! from ..ui.main_ui import UI_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI
        self.setupUi()
        self.initUI()
        # Load the QSS style sheet
        style_sheet_file = QFile("main.qss")
        if style_sheet_file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):
            style_sheet = QTextStream(style_sheet_file).readAll()
            self.setStyleSheet(style_sheet)
        
        # Create other windows objects
        self.calendar_window = Calendar()
        self.weather_window = Weather()


    
    def initUI(self):
        self.btn_to_calendar.pressed.connect(self.show_calendar)
        self.btn_to_weather.pressed.connect(self.show_weather)
    
    def show_calendar(self):
        self.calendar_window.show()
        self.hide

    def show_weather(self):
        self.weather_window.show()
        self.hide()