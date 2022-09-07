from sys import exit
from .gui_login import GUILogin
from .gui_operations_main import GUIOperationsMain
from .objects import app


def execute_app():
    win = GUILogin()
    win.show()
    exit(app.exec())
    