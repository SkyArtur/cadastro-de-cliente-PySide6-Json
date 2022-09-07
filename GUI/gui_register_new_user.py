# -*- coding: utf-8 -*-
from GUI.objects import *
from managers import ManagerNewUser


class GUIRegisterNewUser(MyWidgetStandard):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(301)
        self.setFixedHeight(317)
        self.setWindowTitle('Cadastrar Novo Usuário')
        self.label_top = MyLabelTop(self, 'Cadastrar Novo Usuário')
        self.label_name = MyLabelStandard(self, 'Nome')
        self.label_username = MyLabelStandard(self, 'Username')
        self.label_password = MyLabelStandard(self, 'Password')
        self.label_confirm_password = MyLabelStandard(self, 'Confirm')
        self.label_bottom = MyLabelBottom(self, '\u00a9SkyArtur - 2022')
        self.__name = MyInputStandard(self)
        self.__username = MyInputStandard(self)
        self.__password = MyInputPassword(self)
        self.__confirm = MyInputPassword(self)
        self.button_save_user = MyButtonStandard(self, "Salvar")
        self.button_return = MyButtonStandard(self, "Retornar")
        self.setup_labels(), self.setup_inputs()
        self.setup_buttons()

    @property
    def name(self):
        return self.__name.text().lower()

    @property
    def username(self):
        return self.__username.text().lower()

    @property
    def password(self):
        return self.__password.hash()

    @property
    def confirm(self):
        return self.__confirm.hash()

    def setup_labels(self):
        self.label_name.setGeometry(QRect(20, 70, 41, 31))
        self.label_username.setGeometry(QRect(20, 110, 61, 31))
        self.label_password.setGeometry(QRect(20, 150, 61, 31))
        self.label_confirm_password.setGeometry(QRect(20, 190, 61, 31))
        self.label_top.setGeometry(QRect(20, 10, 261, 41))
        self.label_bottom.setGeometry(QRect(10, 290, 281, 20))

    def setup_inputs(self):
        self.__name.setGeometry(QRect(62, 70, 221, 31))
        self.__username.setGeometry(QRect(82, 110, 201, 31))
        self.__password.setGeometry(QRect(82, 150, 201, 31))
        self.__confirm.setGeometry(QRect(82, 190, 201, 31))

    def setup_buttons(self):
        self.button_save_user.setGeometry(QRect(90, 230, 91, 31))
        self.button_save_user.clicked(self.command_save)
        self.button_return.setGeometry(QRect(190, 230, 91, 31))
        self.button_return.clicked(self.close)

    def command_save(self):
        manager = ManagerNewUser(self.name, self.username, self.password, self.confirm)
        if not manager.valid_username():
            self.__username.clear()
            self.__username.setPlaceholderText("Nome de usuário inválido!")
            return
        elif not manager.confirm_password():
            self.__password.clear()
            self.__confirm.clear()
            self.__password.setPlaceholderText("Senhas não conferem!")
            return
        else:
            manager.save_new_user()
            self.close()
