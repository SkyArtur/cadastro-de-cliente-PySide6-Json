# -*- coding: utf-8 -*-
from .objects import *


class GUIOperationsAccount(MyWidgetStandard):
    def __init__(self, operation):
        super().__init__()
        self.setFixedWidth(330)
        self.setFixedHeight(90)
        self.setWindowTitle('Operações')
        self.group_operation = QGroupBox(self)
        self.group_operation.setTitle(operation)
        self.label_operation = MyLabelStandard(self.group_operation, "Valor")
        self.button_OK = MyButtonStandard(self, "OK")
        self.button_Cancel = MyButtonStandard(self, "Cancelar")
        self.__value = MyInputFloat(self.group_operation)
        self.setup_all(), self.setup_buttons()

    def setup_all(self):
        self.button_OK.setGeometry(QRect(240, 20, 75, 24))
        self.button_Cancel.setGeometry(QRect(240, 50, 75, 24))
        self.group_operation.setGeometry(QRect(10, 10, 221, 71))
        self.label_operation.setGeometry(QRect(8, 20, 41, 41))
        self.__value.setGeometry(QRect(50, 20, 161, 41))

    def setup_buttons(self):
        self.button_OK.clicked(self.command_button_ok)
        self.button_Cancel.clicked(self.close)

    def command_button_ok(self):
        print(self.__value)
