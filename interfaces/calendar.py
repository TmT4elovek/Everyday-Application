from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6.QtCore import *
from PyQt6.QtGui import QIcon

import datetime
import sqlite3

from UI.calendar_ui import Ui_MainWindow
from UI.withoutUser_ui import Ui_MainWindow_WithoutUser
from interfaces.dialogs.info import InfoDialog


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

        # Add items to listwidget
        self.update_events_list()

        # If any item is selected turn on btns
        self.events_list.itemClicked.connect(self.turn_on_btns)

        self.btn_delete.pressed.connect(self.delete_item)
        self.btn_info.pressed.connect(self.info_ab_item)
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
            self.update_events_list()

            # Clear all fields
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
    
    def update_events_list(self):
        #! connect to db
        conn = sqlite3.connect('databases/database.db')
        cur = conn.cursor()
        
        cur.execute(
            '''
                SELECT title, date
                FROM user_events
                WHERE user_id = ?
                ORDER BY date_unix ASC
            ''', (self.home_window.get_user()[0],)
        )
        events = cur.fetchall()
        events = [elem[0] + ' ' * (70 - len(elem[0])) + elem[1] for elem in events]

        self.events_list.clear()

        self.events_list.addItems(events)

    def turn_on_btns(self) -> None:
        if not (self.btn_info.isEnabled() and self.btn_delete.isEnabled()):
            self.btn_info.setEnabled(True)
            self.btn_info.setStyleSheet('background: rgb(115, 115, 173);\\n\nborder: None;\nborder-radius: 6px;')
            self.btn_delete.setEnabled(True)
            self.btn_delete.setStyleSheet('background: rgb(115, 115, 173);\\n\nborder: None;\nborder-radius: 6px;')

    def delete_item(self) -> None:
        if self.confirm('Are you sure you want to delete?'):
            selected_item = self.events_list.selectedItems()[0].text()
            selected_item = selected_item.split(maxsplit=1)

            #! connect to db
            conn = sqlite3.connect('databases/database.db')
            cur = conn.cursor()
            
            cur.execute(
                '''
                    DELETE FROM user_events
                    WHERE user_id = ? AND title = ? AND date = ?
                ''', (self.home_window.get_user()[0], selected_item[0], selected_item[1])
            )

            conn.commit()
            #! close connection
            conn.close()

            self.update_events_list()

    def confirm(self, text: str) -> bool:
        # Dialog for confirmation action
        dlg = QMessageBox(self)
        dlg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        dlg.setWindowTitle("Confirm")
        dlg.setText(text)
        button = dlg.exec()
        if button == QMessageBox.StandardButton.Ok:
            return True
        else:
            return False
    
    def info_ab_item(self) -> None:
        selected_item = self.events_list.selectedItems()[0].text()
        selected_item = selected_item.split(maxsplit=1)
        title = selected_item[0]
        date = datetime.datetime.strptime(selected_item[1], '%Y-%m-%d %H:%M')

        info_dialog = InfoDialog(title, date, self)
        if info_dialog.exec():
            print(info_dialog.data)
            if info_dialog.data:
                self.update_event_in_db(self.home_window.get_user()[0],
                                        title, info_dialog.data['title'], 
                                        info_dialog.data['date'], 
                                        datetime.datetime.timestamp(date), 
                                        info_dialog.data['date_unix']
                                        )
                self.update_events_list()
        
    def update_event_in_db(self, user_id: int, title:str, title_new: str, date_new: str, date_unix: int, date_unix_new: int) -> None:
        #! connect to db
        conn = sqlite3.connect('databases/database.db')
        cur = conn.cursor()
        
        cur.execute(
            '''
                UPDATE user_events
                SET title = ?, date = ?, date_unix = ?
                WHERE user_id = ? AND title = ? AND date_unix = ?
            ''', (title_new, date_new, date_unix_new, user_id, title, date_unix)
        )

        conn.commit()
        #! close connection
        conn.close()