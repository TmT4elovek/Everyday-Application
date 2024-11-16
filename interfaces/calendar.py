from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import *
from PyQt6.QtGui import QIcon

import datetime
import sqlite3

from UI.calendar_ui import Ui_MainWindow
from UI.withoutUser_ui import Ui_MainWindow_WithoutUser


class Calendar(QMainWindow, Ui_MainWindow, Ui_MainWindow_WithoutUser):
    def __init__(self, home_window: object) -> None:
        super().__init__(home_window)
        # Save the home window reference
        self.home_window = home_window

        if self.home_window.get_user():
            # Load the UI file
            self.setupUi(self)
            self.initUI()
        else:
            self.setupUi_withoutUser(self)

        # Set button_home icon
        self.btn_home.setIcon(QIcon("items\icons\home.png"))
        self.btn_home.pressed.connect(self.to_home)

    def initUI(self) -> None:
        self.btn_add_event.pressed.connect(self.add_event)

    def to_home(self) -> None:
        # Close the current window
        self.hide()
        # Open the main window here
        self.home_window.show()

    # If this window closed quit app
    def closeEvent(self, event) -> None:
        print('Calendar window closed')
        QCoreApplication.quit()
        event.accept()

    def add_event(self) -> None:
        title = self.event_edit.text()
        if title:
            self.err_label.setText('')

            date = self.calendar.selectedDate().toPyDate()
            time = self.time_edit.time().toPyTime()

            full_date = datetime.datetime.combine(date, time)
            dt_unix = int(datetime.datetime.timestamp(full_date))
            full_date_str = datetime.datetime.strftime(full_date, '%Y-%m-%d %H:%M')

            self.add_event_to_db(self.home_window.get_user()[0], title, full_date_str, dt_unix)

            self.event_edit.clear()
            self.calendar.setSelectedDate(datetime.date.today())
            self.time_edit.setTime(datetime.time(0, 0))
        else:
            self.err_label.setText('Enter an event')

    def add_event_to_db(self, user_id: int, title: str, date: str, date_unix: int) -> None:
        #! connect to db
        conn = sqlite3.connect('databases/database.db')
        cur = conn.cursor()
        
        cur.execute(
            '''
                INSERT INTO user_events (user_id, title, date, date_unix)
                VALUES (?, ?, ?, ?)
            ''', (user_id, title, date, date_unix)
        )
        conn.commit()
        #! close connection
        conn.close()