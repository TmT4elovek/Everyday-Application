from PyQt6.QtWidgets import QDialog

import sqlite3

from UI.log_in_ui import Ui_Dialog


class LogIn(QDialog, Ui_Dialog):
    def __init__(self, MainWindow: object):
        super().__init__(MainWindow)

        self.setupUi(self)
        self.initUI()
        self.setModal(True)  # Make the dialog modal, so it blocks the main window until it's closed

        self.main_w = MainWindow
    
    def initUI(self) -> None:
        self.btn_to_reg.pressed.connect(self.to_reg)
        self.btn_enter.pressed.connect(self.enter)

    def to_reg(self) -> None:
        self.main_w.register()
        self.close()
    
    def enter(self) -> None:
        username = self.username_edit.text()
        password = self.password_edit.text()

        #! connect to db
        conn = sqlite3.connect('databases/database.db')
        cur = conn.cursor()

        # check if user exists
        user: tuple = cur.execute(
            '''
                SELECT *
                FROM user
                WHERE username = ? AND password = ?
            ''', (username, password)).fetchone()
        
        if not user:
            self.err_label.setText('Неверное имя пользователя или пароль!')
            self.username_edit.clear()
            self.password_edit.clear()
            return
        
        self.main_w.set_user(user)
        #! close connection
        conn.close()

        self.main_w.check_user()

        self.close()