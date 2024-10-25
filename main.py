import sys
from PyQt6.QtWidgets import QApplication

from main import Main


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())