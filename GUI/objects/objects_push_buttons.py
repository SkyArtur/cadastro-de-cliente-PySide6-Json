# -*- coding: utf-8 -*-
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QIcon
from pycep_correios import get_address_from_cep, WebService, exceptions


class MyButtonStandard(QPushButton):
    def __init__(self, parent, text=None):
        QPushButton.__init__(self, parent=parent, text=text)
        self.setProperty('class', 'buttons')
        font = QFont()
        font.setPointSize(10)
        self.setFont(font)
        self.setStyleSheet("""
        .buttons{
            border: 2px solid;
            background-color: rgb(227, 227, 227);
            border-color: rgb(210, 210, 210);
            border-radius: 10px;
            }
            .buttons:pressed{
            border: 2px solid;
            border-color: rgb(220, 220, 220);
            }""")

    def keyPressEvent(self, e):
        super(MyButtonStandard, self).keyPressEvent(e)
        if e.key() == Qt.Key.Key_Return or e.key() == Qt.Key.Key_Enter:
            self.focusNextChild()

    def clicked(self, function):
        super(MyButtonStandard, self).clicked.connect(function)


class MyButtonSearchCEP(QPushButton):

    def __init__(self, parent, *inputs):
        super().__init__(parent=parent)
        self.setProperty('class', 'buttons')
        font = QFont()
        font.setPointSize(10)
        self.setFont(font)
        self.setStyleSheet("""
        .buttons{
            border: 2px solid;
            background-color: rgb(235, 235, 235);
            border-color: rgb(210, 210, 210);
            border-radius: 10px;
        }
        .buttons:pressed{
            border: 2px solid;
            border-color: rgb(220, 220, 220);
        }""")
        icon_lupa = QIcon()
        icon_lupa.addFile("lupa.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.setIcon(icon_lupa)
        self.cep = inputs[0]
        self.street = inputs[1]
        self.neighborhood = inputs[2]
        self.city = inputs[3]
        self.state = inputs[4]

    def searchCEP(self):
        try:
            cep = get_address_from_cep(self.cep.text(), webservice=WebService.VIACEP)
        except exceptions.BaseException:
            pass
        except ValueError:
            pass
        else:
            self.street.setText(cep['logradouro'])
            self.neighborhood.setText(cep['bairro'])
            self.city.setText(cep['cidade'])
            self.state.setText(cep['uf'])

    def keyPressEvent(self, e):
        super(MyButtonSearchCEP, self).keyPressEvent(e)
        if e.key() == Qt.Key.Key_Return or e.key() == Qt.Key.Key_Enter:
            self.searchCEP()

    def clicked(self):
        super(MyButtonSearchCEP, self).clicked.connect(self.searchCEP)
