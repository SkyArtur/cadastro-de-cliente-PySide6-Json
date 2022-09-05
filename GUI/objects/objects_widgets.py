from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QIcon, QFont
from PySide6.QtCore import QSize


class MyWidgetStandard(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        icon = QIcon()
        icon.addFile('./GUI/icon/py.ico', QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.font = QFont()
        self.font.setPointSize(14)
        self.font1 = QFont()
        self.font1.setPointSize(10)
        self.font2 = QFont()
        self.font2.setPointSize(8)
        self.font3 = QFont()
        self.font3.setPointSize(7)
        self.setFont(self.font2)

    def command_exit_program(self):
        exit(QApplication.exec())
