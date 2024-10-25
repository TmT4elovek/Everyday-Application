from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic


class Weather(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI file
        uic.loadUi('weather.ui', self)

        self.initUI()
    
    def initUI(self):
        pass