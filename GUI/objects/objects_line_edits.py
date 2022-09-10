# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from hashlib import sha256
import re


class MyInputStandard(QLineEdit):
    def __init__(self, parent):
        QLineEdit.__init__(self, parent=parent)
        font = QFont()
        font.setPointSize(10)
        self.setFont(font)
        self.setStyleSheet("""
        padding-left: 5px;
        border: 2px solid;
        border-radius: 10px;
        border-color: rgb(210, 210, 210);""")

    def __str__(self):
        return self.text()

    def keyPressEvent(self, e):
        super(MyInputStandard, self).keyPressEvent(e)
        if e.key() == Qt.Key.Key_Return or e.key() == Qt.Key.Key_Enter:
            self.focusNextChild()


class MyInputFloat(MyInputStandard):
    def __init__(self, parent):
        super().__init__(parent)
        self.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.setPlaceholderText("0,00")

    def focusOutEvent(self, e):
        super(MyInputFloat, self).focusOutEvent(e)
        self.valid_input()

    @property
    def value_input(self):
        return float(self.text().replace(',', '.'))

    def valid_input(self):
        try:
            float(self.text().replace(',', '.'))
        except ValueError:
            self.clear()
            self.setPlaceholderText("Valor Inválido")
            return False
        else:
            return True

    def __add__(self, other):
        return self.value_input + other

    def __lt__(self, other):
        return self.value_input < other

    def __le__(self, other):
        return self.value_input <= other

    def __eq__(self, other):
        return self.value_input == other

    def __ne__(self, other):
        return self.value_input != other

    def __gt__(self, other):
        return self.value_input > other

    def __ge__(self, other):
        return self.value_input >= other


class MyInputPassword(MyInputStandard):
    def __init__(self, parent):
        super().__init__(parent)
        self.setEchoMode(QLineEdit.Password)

    def __str__(self):
        return sha256(bytes((str(self.text())), "utf-8")).hexdigest()

    def hash(self):
        return sha256(bytes((str(self.text())), "utf-8")).hexdigest()


class MyInputCEP(MyInputStandard):
    def __init__(self, parent):
        super().__init__(parent)
        self.__cep_valid = None
        self.setPlaceholderText("ex.:80050555")

    def valid_input(self):
        try:
            self.__cep_valid = re.search("([0-9]{5})-?([0-9]{3})$", self.text())
            self.__cep_valid = f"{self.__cep_valid.group(1)}-{self.__cep_valid.group(2)}"
        except AttributeError:
            self.clear()
            self.setPlaceholderText('CEP inválido')
        else:
            self.setText(self.__cep_valid)

    def focusOutEvent(self, e):
        super(MyInputCEP, self).focusOutEvent(e)
        self.valid_input()

    def __str__(self):
        return self.__cep_valid


class MyInputCPF(MyInputStandard):
    def __init__(self, parent):
        super().__init__(parent)
        self.__cpf_valid = None
        self.setPlaceholderText("ex.:01402501400")

    def valid_input(self):
        non_zeros = ""
        try:
            cpf = re.search("([0-9]{3}).?([0-9]{3}).?([0-9]{3})-?([0-9]{2})$", self.text())
            for digits in cpf.groups():
                non_zeros += digits
            if "00000000000" == non_zeros:
                raise AttributeError
            self.__cpf_valid = f"{cpf.group(1)}.{cpf.group(2)}.{cpf.group(3)}-{cpf.group(4)}"
        except AttributeError:
            self.clear()
            self.setPlaceholderText('CPF inválido')
        else:
            self.setText(self.__cpf_valid)

    def focusOutEvent(self, e):
        super(MyInputCPF, self).focusOutEvent(e)
        self.valid_input()

    def __str__(self):
        return self.__cpf_valid


class MyInputPhone(MyInputStandard):
    def __init__(self, parent):
        super().__init__(parent)
        self.__phone = self.text()
        self.setPlaceholderText("ex.:42990001111")

    def valid_phone(self):
        try:
            self.__phone = re.search("^(0?[1-9]{2})([0-9]{4,5})-?([0-9]{4})$", self.text())
            self.__phone = f"({self.__phone.group(1)}) {self.__phone.group(2)}-{self.__phone.group(3)}"
        except AttributeError:
            self.clear()
            self.setPlaceholderText('Número inválido')
        else:
            self.setText(self.__phone)

    def focusOutEvent(self, e):
        super(MyInputPhone, self).focusOutEvent(e)
        self.valid_phone()

    def __str__(self):
        return self.__phone
