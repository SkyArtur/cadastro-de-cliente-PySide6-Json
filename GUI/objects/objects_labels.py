# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class MyLabelStandard(QLabel):
    def __init__(self, parent, text=None):
        super().__init__(parent=parent, text=text)
        font = QFont()
        font.setPointSize(8)
        self.setFont(font)


class MyLabelTop(MyLabelStandard):
    def __init__(self, parent, text=None):
        super().__init__(parent, text)
        font = QFont()
        font.setPointSize(14)
        self.setFont(font)
        self.setAlignment(Qt.AlignCenter)


class MyLabelBottom(MyLabelStandard):
    def __init__(self, parent, text=None):
        super().__init__(parent, text)
        font = QFont()
        font.setPointSize(7)
        self.setFont(font)
        self.setAlignment(Qt.AlignCenter)


class MyLabelMessages(MyLabelStandard):
    def __init__(self, parent, text=None):
        super().__init__(parent, text)
        font = QFont()
        font.setPointSize(10)
        self.setFont(font)
        self.setAlignment(Qt.AlignCenter)
