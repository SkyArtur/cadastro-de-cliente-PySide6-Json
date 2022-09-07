# -*- coding: utf-8 -*-
from .gui_register_new_user import GUIRegisterNewUser
from .gui_operations_main import GUIOperationsMain
from .objects import *
from managers import ManagerLogin


class GUILogin(MyWidgetStandard):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(279)
        self.setFixedHeight(282)
        self.setWindowTitle('Login')
        self.main_operations = None
        self.register_new_user = None
        self.label_top = MyLabelTop(self, "LOGIN")
        self.label_message = MyLabelMessages(self)
        self.label_bottom = MyLabelBottom(self, "\u00a9SkyArtur - 2022")
        self.button_login = MyButtonStandard(self, "Login")
        self.button_register = MyButtonStandard(self, "Novo Usuário")
        self.__username = MyInputStandard(self)
        self.__password = MyInputPassword(self)
        self.setup_labels(), self.setup_buttons()
        self.setup_inputs()

    def setup_labels(self):
        self.label_top.setGeometry(QRect(20, 10, 241, 31))
        self.label_message.setGeometry(QRect(10, 130, 261, 31))
        self.label_bottom.setGeometry(QRect(0, 260, 271, 21))

    def setup_inputs(self):
        self.__username.setGeometry(QRect(20, 50, 241, 31))
        self.__username.setPlaceholderText('Username')
        self.__password.setGeometry(QRect(20, 90, 241, 31))
        self.__password.setPlaceholderText('Password')

    def setup_buttons(self):
        font = QFont()
        font.setPointSize(8)
        self.button_login.setGeometry(QRect(80, 170, 121, 31))
        self.button_register.setGeometry(80, 210, 121, 31)
        self.button_register.setFont(font)
        self.button_login.clicked(self.command_login)
        self.button_register.clicked(self.command_register)

    def command_login(self):
        manager = ManagerLogin(self.__username.text(), self.__password.hash())
        if manager.valid_password():
            if self.main_operations is None:
                self.main_operations = GUIOperationsMain()
                self.main_operations.show()
                self.close()
        else:
            self.__username.clear()
            self.__password.clear()
            self.label_message.setText("Senha ou usuário inválidos!")
            self.label_message.setStyleSheet('color: red;')

    def command_register(self):
        if self.register_new_user is None:
            self.register_new_user = GUIRegisterNewUser()
            self.register_new_user.show()
            self.__username.clear()
            self.__password.clear()
        else:
            self.register_new_user.close()
            self.register_new_user = None
