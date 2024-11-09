from PyQt6.QtWidgets import QMainWindow

from PyQt6.QtCore import QFile, QIODevice, QTextStream, QCoreApplication

from interfaces.calendar import Calendar
from interfaces.weather_window import Weather

from UI.main_ui import Ui_MainWindow
from interfaces.dialogs.register import Register

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

        #Create dialog window
        self.register_dialog = Register()


    
    def initUI(self) -> None:
        self.btn_to_calendar.pressed.connect(self.show_calendar)
        self.btn_to_weather.pressed.connect(self.show_weather)

        self.btn_register.pressed.connect(self.register)
    
    def show_calendar(self) -> None:
        self.calendar_window.show()
        self.hide()

    def show_weather(self) -> None:
        self.weather_window.show()
        self.hide()

    def closeEvent(self, event) -> None:
        QCoreApplication.quit()
        event.accept()

    def register(self) -> None:
        self.register_dialog.show()