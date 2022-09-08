from sys import exit
from .gui_login import GUILogin
from .objects import app


def execute_app():
    win = GUILogin()
    win.show()
    exit(app.exec())
    