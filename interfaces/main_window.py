from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QCoreApplication, QThread
from PyQt6.QtGui import QIcon

import datetime
import time

from interfaces.calendar import Calendar
from interfaces.weather_window import Weather

from UI.main_ui import Ui_MainWindow
from interfaces.dialogs.register import Register
from interfaces.dialogs.log_in import LogIn


class TaskThread(QThread):
    def __init__(self, foo):
        super().__init__()
        self.foo = foo
    
    def run(self):
        self.foo()


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        #userdata
        self._user = ()
        self.today_weather_icon = ''

        # Load the UI
        self.setupUi(self)
        self.initUI()
        
        # Create other windows objects
        self.calendar_window = Calendar(self)
        self.weather_window = Weather(self)

        #Create dialog window
        self.register_dialog = Register(self)
        self.log_in_dialog = LogIn(self)

        # Add thread for clock
        self.clock_thread = TaskThread(self.clock_work)
        self.clock_thread.start()

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

    def set_user(self, user: tuple) -> None:
        self._user = user

    def get_user(self) -> tuple:
        return self._user

    def check_user(self) -> None:
        if self._user:
            self.nickname_label.setText(self._user[1])
            self.btn_register.setText('')
            self.btn_register.setIcon(QIcon('items\icons\log_out.png'))
            self.btn_register.pressed.connect(self.log_out)

            self.weather_window.__init__(self)
            self.calendar_window.__init__(self)
            self.btn_to_weather.setIcon(QIcon(f'items\weather_icons\{self.today_weather_icon}.png'))
        else:
            self.nickname_label.setText('')
            self.btn_register.setText('Sign up')
            self.btn_register.setIcon(QIcon())
            self.btn_register.pressed.connect(self.register)

            self.weather_window.__init__(self)
            self.calendar_window.__init__(self)
            self.btn_to_weather.setIcon(QIcon(f'items\weather_icons\{self.today_weather_icon}.png'))
        
    def log_out(self) -> None:
        self._user = ()
        self.check_user()

    def clock_work(self):
        while True:
            now = datetime.datetime.now()
            self.clock.setText(f'{now.hour:02}:{now.minute:02}')
            time.sleep(60)