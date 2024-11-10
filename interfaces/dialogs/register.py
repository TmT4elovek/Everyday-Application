import sqlite3

from PyQt6.QtWidgets import QDialog

from UI.register_ui import Ui_Dialog


class Register(QDialog, Ui_Dialog):
    def __init__(self, MainWindow: object) -> None:
        super().__init__(MainWindow)

        self.setupUi(self)
        self.initUI()
        self.setModal(True) # Make the dialog modal, so it blocks the main window until it's closed

        self.main_w = MainWindow

    def initUI(self) -> None:
        # Get from bd countries
        #! connect to db
        conn = sqlite3.connect('databases/database.db')
        cur = conn.cursor()

        self.countries: list[tuple] = cur.execute(
            '''
                SELECT DISTINCT country
                FROM worldcities
                ORDER BY country
            '''
        ).fetchall()

        self.countries: list[str] = [elem[0] for elem in self.countries]
        #! close connection
        conn.close()

        # add countries to combobox
        self.country_combo.addItems(self.countries)
        # change city_combo if country was changed
        self.country_combo.currentTextChanged.connect(self.on_country_changed)

        # connect reg btn
        self.btn_register.clicked.connect(self.on_register_clicked)

        # connect logIn btn
        self.btn_logIn.clicked.connect(self.on_logIn)

    # Changed country_combo
    def on_country_changed(self) -> None:
        city = self.get_city()
        self.city_combo.clear()
        self.city_combo.addItems(city)

    def get_city(self) -> list:
        #! connect to db
        conn = sqlite3.connect('databases/database.db')
        cur = conn.cursor()

        city: list[tuple] = cur.execute('''
            SELECT city
            FROM worldcities
            WHERE country = ?
            GROUP BY city
        ''', (self.country_combo.currentText(),)
        ).fetchall()

        city: list[str] = [elem[0] for elem in city]
        #! close connection
        conn.close()

        return city

    def on_register_clicked(self) -> None:
        # get user data
        username = self.nickname_edit.text()
        password = self.password_edit.text()
        sec_password = self.sec_password_edit.text()
        city = self.city_combo.currentText()

        if not self.is_nickname_corr(username):
            self.err_label.setText('Имя пользователя должно содержать только буквы и цифры')
            self.nickname_edit.clear()
            return

        if not self.is_password_corr(password):
            self.err_label.setText('Пароль должен содержать не менее 8 символов, содержать хотя бы одну большую букву, одну маленькую букву и одну цифру')
            self.password_edit.clear()
            self.sec_password_edit.clear()
            return

        if password != sec_password:
            self.err_label.setText('Пароли не совпадают')
            self.password_edit.clear()
            self.sec_password_edit.clear()
            return
        
        #! connect to db
        conn = sqlite3.connect('databases/database.db')
        cur = conn.cursor()

        # check if user exists
        user: tuple = cur.execute(
            '''
                SELECT *
                FROM user
                WHERE username = ?
            ''', (username,)
        ).fetchone()

        if not user is None:
            self.err_label.setText('Пользователь с таким именем уже существует')
            self.nickname_edit.clear()
            return
        
        # create user
        cur.execute(
            '''
                INSERT INTO user (username, password, city_id)
                VALUES (?, ?, ?)
            ''', (username, password, self.get_city_id(city),)
        )
        conn.commit()

        #! close connection
        conn.close()

        self.main_w.log_in()
        self.close()

    def get_city_id(self, city: str) -> int:
        #! connect to db
        conn = sqlite3.connect('databases/database.db')
        cur = conn.cursor()
        
        city_id: tuple = cur.execute('''
            SELECT id
            FROM worldcities
            WHERE city = ?
        ''', (city,)
        ).fetchone()

        #! close connection
        conn.close()

        return city_id[0]
    
    def is_password_corr(self, password: str) -> bool:
        return len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password)
    
    def is_nickname_corr(self, nickname: str) -> bool:
        return nickname.isalnum()
    
    # Go to logIn dialog
    def on_logIn(self) -> None:
        self.main_w.log_in()
        self.close()