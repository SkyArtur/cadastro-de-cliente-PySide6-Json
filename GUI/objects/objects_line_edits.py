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

    def focusOutEvent(self, e):
        super(MyInputFloat, self).focusOutEvent(e)
        self.valid_input()

    def __str__(self):
        return self.text().replace(',', '.')

    def valid_input(self):
        try:
            float(self.text().replace(',', '.'))
        except ValueError:
            self.clear()
            self.setPlaceholderText("Valor Inválido")
            return False
        else:
            return True


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

    def valid_input(self):
        self.__cep_valid = re.search("([0-9]{5})-?([0-9]{3})", self.text())
        if self.__cep_valid is None or len(self.text()) > 8:
            self.clear()
            self.setPlaceholderText('Número inválido')
        else:
            self.__cep_valid = f"{self.__cep_valid.group(1)}-{self.__cep_valid.group(2)}"
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

    def valid_input(self):
        cpf = re.search("([0-9]{3}).?([0-9]{3}).?([0-9]{3})-?([0-9]{2})", self.text())
        if cpf is None or len(self.text()) > 11:
            self.clear()
            self.setPlaceholderText('Número inválido')
        else:
            self.__cpf_valid = f"{cpf.group(1)}.{cpf.group(2)}.{cpf.group(3)}-{cpf.group(4)}"
            self.setText(self.__cpf_valid)

    def focusOutEvent(self, e):
        super(MyInputCPF, self).focusOutEvent(e)
        self.valid_input()

    def __str__(self):
        return self.__cpf_valid
