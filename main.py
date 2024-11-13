import sys
from PyQt6.QtWidgets import QApplication

from interfaces.main_window import Main


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Create the main window and show it
    main_window = Main()
    main_window.show()
    # Close window
    sys.exit(app.exec())



    #!!!!! Спросить почему питон не видит getter method класса Main в Weather(метод get_response 126 Строчка)
    #!!!!! Спросить как реализовать часы на главном окне