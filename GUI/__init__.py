from sys import exit
from GUI.gui_login import GUILogin
from GUI.objects import app


def execute_app():
    win = GUILogin()
    win.show()
    exit(app.exec())
    