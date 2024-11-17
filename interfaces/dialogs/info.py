from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtCore import QDate, QTime

import datetime

from UI.info_ui import Ui_Dialog



class InfoDialog(QDialog, Ui_Dialog):
    def __init__(self, title: str, date: datetime.datetime, parent: object) -> None:
        super().__init__(parent=parent)

        self.title = title
        self.date = date
        self.data = {}

        self.setupUi(self)
        self.initUI()
        self.setModal(True)  # Make the dialog modal, so it blocks the main window until it's closed
        
    def initUI(self) -> None:
        self.event_edit.setText(self.title)
        self.dateEdit.setDate(QDate(self.date.year, self.date.month, self.date.day))
        self.timeEdit.setTime(QTime(self.date.hour, self.date.minute))

        self.btn_save.pressed.connect(self.save)
        self.btn_cancel.pressed.connect(self.cancel)
    

    def confirm(self, text: str) -> bool:
        dlg = QMessageBox(self)
        dlg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        dlg.setWindowTitle("Confirm")
        dlg.setText(text)
        button = dlg.exec()
        if button == QMessageBox.StandardButton.Ok:
            return True
        else:
            return False
    
    def save(self) -> None:
        date = datetime.datetime(
            self.dateEdit.date().year(),
            self.dateEdit.date().month(), 
            self.dateEdit.date().day(), 
            self.timeEdit.time().hour(), 
            self.dateEdit.time().minute()
        )

        if self.title != self.event_edit.text() or self.date != date:
            self.data['title'] = self.event_edit.text()
            self.data['date'] = date
            self.data['date_unix'] = datetime.datetime.timestamp(self.data['date'])
        self.accept()
    
    def cancel(self) -> None:
        if self.confirm("Save changes?"):
            self.save()
        else:
            self.accept()