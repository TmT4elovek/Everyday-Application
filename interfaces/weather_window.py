import requests
import datetime

import sqlite3

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QIcon, QImage, QPixmap

from UI.weather_ui import Ui_MainWindow
from UI.withoutUser_ui import Ui_MainWindow_WithoutUser
from SECRET import API_KEY

class Weather(QMainWindow, Ui_MainWindow, Ui_MainWindow_WithoutUser):
    def __init__(self, home_window: object) -> None:
        super().__init__(home_window)

        # Save the home window reference
        self.home_window = home_window
        if self.home_window.get_user():
            try:
                #Api request
                self.get_response()

                # Load the UI file
                self.setupUi(self)
                self.initUI()
            except requests.exceptions.ConnectTimeout:
                print('Api no response. Try to use VPN')
                home_window.log_out()
            # except requests.exceptions.
        else:
            self.setupUi_withoutUser(self)
        # btn back to main connect
        self.btn_home.pressed.connect(self.to_home)

    def initUI(self) -> None:
        self.btn_home.setIcon(QIcon("items\icons\home.png"))

        self.weekdays = {
            0: 'Monday',
            1: 'Tuesday',
            2: 'Wednesday',
            3: 'Thursday',
            4: 'Friday',
            5: 'Saturday',
            6: 'Sunday'
        }
        
        self.months = {
            1: 'January',
            2: 'February',
            3: 'March',
            4: 'April',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'August',
            9: 'September',
            10: 'October',
            11: 'November',
            12: 'December'
        }

        self.weather_widgets = {
            'day_of_week_1': self.day_of_week_1,
            'date_1': self.date_1,
            'weather_icon_1': self.weather_icon_1,
            'temp_day_1': self.temp_day_1,
            'weather_1': self.weather_1,

            'day_of_week_2': self.day_of_week_2,
            'date_2': self.date_2,
            'weather_icon_2': self.weather_icon_2,
            'temp_day_2': self.temp_day_2,
            'weather_2': self.weather_2,

            'day_of_week_3': self.day_of_week_3,
            'date_3': self.date_3,
            'weather_icon_3': self.weather_icon_3,
            'temp_day_3': self.temp_day_3,
            'weather_3': self.weather_3,

            'day_of_week_4': self.day_of_week_4,
            'date_4': self.date_4,
            'weather_icon_4': self.weather_icon_4,
            'temp_day_4': self.temp_day_4,
            'weather_4': self.weather_4
        }

        # Set city
        self.city.setText(f'Weather in {self.get_user_city(self.home_window.get_user())[1]}')

        ######## TODAY ########
        weather = self.dates[0]['weather'][0]
        wind = self.dates[0]['wind']
        main = self.dates[0]['main']

        # today temp
        temp = round(main['temp'])
        self.temp.setText(f"+{temp}") if temp >= 0 else self.temp.setText(f"-{temp}")
        temp_like = round(self.dates[0]['main']['feels_like'])
        self.temp_like.setText(f'Feels like {temp_like}')

        # Set today icon
        self.weather_icon_5.setPixmap(QPixmap(QImage(f'items\weather_icons\{weather["icon"]}.png')))

        # Set wind
        self.wind.setText(f'{wind["speed"]} mps, {self.conv_deg_to_ws(wind["deg"])}')

        # Set humidity
        self.humidity.setText(f'{main["humidity"]}%')

        # Set pressure
        self.pressure.setText(f'{main["pressure"]} mm Hg')

        #Set weather discription
        self.weather.setText(weather['description'].title())

        ######## SET OTHER WIDGETS #####
        for i in range(1, 5):
            self.set_weather_widget(i)

    def to_home(self) -> None:
        # Close the current window
        self.hide()
        # Open the main window here
        self.home_window.show()
    
    def closeEvent(self, event) -> None:
        QCoreApplication.quit()
        event.accept()

    def get_response(self) -> None:
        #get city
        city = self.get_user_city(self.home_window.get_user())
        lat = city[3]
        lon = city[4]

        # API request
        response = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric', stream=True, timeout=10)
        response.raise_for_status()
        data = response.json()
        self.dates = list()
        # Pick only unic days
        for i in range(len(data['list'])):
            dt_unix = data['list'][i]['dt']
            day = datetime.datetime.utcfromtimestamp(dt_unix).day
            if len(self.dates) == 0:
                self.dates.append(data['list'][i])
            
            if day not in [datetime.datetime.utcfromtimestamp(x['dt']).day for x in self.dates]:
                self.dates.append(data['list'][i])

    def get_user_city(self, user) -> tuple:
        # get user city from database
        #! connect to db
        conn = sqlite3.connect('databases/database.db')
        cur = conn.cursor()

        city: tuple = cur.execute(
            '''
                SELECT *
                FROM worldcities
                WHERE id = ?
            ''', (user[-1],)).fetchone()
        
        #! close connection
        conn.close()

        return city

    def conv_deg_to_ws(self, deg: int) -> str:
        if 337 <= deg <= 360 or 0 <= deg <= 22:
            return 'N'
        elif 22 <= deg <= 67:
            return 'NW'
        elif 67 <= deg <= 112:
            return 'W'
        elif 112 <= deg <= 157:
            return 'SW'
        elif 157 <= deg <= 202:
            return 'S'
        elif 202 <= deg <= 247:
            return 'SE'
        elif 247 <= deg <= 292:
            return 'E'
        elif 292 <= deg <= 337:
            return 'NE'

    def set_weather_widget(self, score: int) -> None:
        weather = self.dates[score]['weather'][0]
        main = self.dates[score]['main']
        dt = datetime.datetime.utcfromtimestamp(self.dates[score]['dt'])

        # temp
        temp = round(main['temp'])
        self.weather_widgets[f'temp_day_{score}'].setText(f"+{temp}") if temp >= 0 else self.weather_widgets[f'temp_day_{score}'].setText(f"-{temp}")

        # Set icon
        self.weather_widgets[f'weather_icon_{score}'].setPixmap(QPixmap(QImage(f'items\weather_icons\{weather["icon"]}.png')))

        # Set weather discription
        self.weather_widgets[f'weather_{score}'].setText(weather['description'].title())

        # Set weekday
        self.weather_widgets[f'day_of_week_{score}'].setText(self.weekdays[dt.weekday()])

        # Set date
        self.weather_widgets[f'date_{score}'].setText(f'{dt.day} {self.months[dt.month]}')