from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QFile, QIODevice, QTextStream, QCoreApplication
from PyQt6.QtGui import QIcon

from interfaces.calendar import Calendar
from interfaces.weather_window import Weather

from UI.main_ui import Ui_MainWindow
from interfaces.dialogs.register import Register
from interfaces.dialogs.log_in import LogIn

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
        self.register_dialog = Register(self)
        self.log_in_dialog = LogIn(self)

        #userdata
        self.__user = tuple()

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

    def log_in(self) -> None:
        self.log_in_dialog.show()

    @property
    def user(self) -> tuple:
        return self.__user

    @user.setter
    def user(self, user: tuple) -> None:
        self.__user = user

    def check_user(self) -> None:
        if self.__user:
            self.nickname_label.setText(self.user[1])
            self.btn_register.setText('')
            self.btn_register.setIcon(QIcon('items\icons\log_out.png'))
            self.btn_register.pressed.connect(self.log_out)
        else:
            self.nickname_label.setText('')
            self.btn_register.setText('Sign up')
            self.btn_register.setIcon(QIcon())
            self.btn_register.pressed.connect(self.register)
        
    def log_out(self) -> None:
        self.__user = ()
        self.check_user()