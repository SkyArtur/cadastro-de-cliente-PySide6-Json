from PySide6.QtWidgets import QApplication
from sys import exit, argv
from .gui_login import GUILogin


def execute_app():
    app = QApplication(argv)
    win = GUILogin()
    win.show()
    exit(app.exec())
    