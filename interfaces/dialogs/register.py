from PyQt6.QtWidgets import QDialog

from UI.register_ui import Ui_Dialog


class Register(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.initUI()

    def initUI(self):
        pass