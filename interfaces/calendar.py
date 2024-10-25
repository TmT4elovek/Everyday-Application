from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic


class Calendar(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the UI file
        uic.loadUi('calendar.ui', self)

        self.initUI()
    
    def initUI(self):
        pass