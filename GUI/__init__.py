from PySide6.QtWidgets import QApplication
from sys import exit, argv
from .gui_login import GUILogin
from .gui_operations_main import GUIOperationsMain
from .objects import app


def execute_app():
    win = GUIOperationsMain()
    win.show()
    exit(app.exec())
    