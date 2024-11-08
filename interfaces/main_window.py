from PyQt6.QtWidgets import QMainWindow

from PyQt6.QtCore import QFile, QIODevice, QTextStream, QCoreApplication

from interfaces.calendar import Calendar
from interfaces.weather_window import Weather

from UI.main_ui import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI
        self.setupUi(self)
        self.initUI()
        # Load the QSS style sheet
        #! возможно, придется удалить, тк не будет иметь смысловой нагрузки
        style_sheet_file = QFile("main.qss")
        if style_sheet_file.open(QIODevice.OpenModeFlag.ReadOnly | QIODevice.OpenModeFlag.Text):
            style_sheet = QTextStream(style_sheet_file).readAll()
            self.setStyleSheet(style_sheet)
        
        # Create other windows objects
        self.calendar_window = Calendar(self)
        self.weather_window = Weather(self)


    
    def initUI(self):
        self.btn_to_calendar.pressed.connect(self.show_calendar)
        self.btn_to_weather.pressed.connect(self.show_weather)
    
    def show_calendar(self):
        self.calendar_window.show()
        self.hide()

    def show_weather(self):
        self.weather_window.show()
        self.hide()

    def closeEvent(self, event):
        QCoreApplication.quit()
        event.accept()