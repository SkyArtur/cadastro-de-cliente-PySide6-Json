# -*- coding: utf-8 -*-
from .objects import *


class GUIOperationsDataClient(MyWidgetStandard):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(540)
        self.setFixedHeight(180)
        self.setFont(self.font2)
        self.setWindowTitle('Atualizar dados do Cliente')
        self.Table_Changes = QTabWidget(self)
        self.tab_change_address = QWidget()
        self.tab_change_personal_data = QWidget()
        self.__cep = MyInputCEP(self.tab_change_address)
        self.__street = MyInputStandard(self.tab_change_address)
        self.__home_number = MyInputStandard(self.tab_change_address)
        self.__neighborhood = MyInputStandard(self.tab_change_address)
        self.__city = MyInputStandard(self.tab_change_address)
        self.__state = MyInputStandard(self.tab_change_address)
        self.__name = MyInputStandard(self.tab_change_personal_data)
        self.__email = MyInputStandard(self.tab_change_personal_data)
        self.__phone = MyInputStandard(self.tab_change_personal_data)
        self.button_add_address = MyButtonStandard(self.tab_change_address, "Adicionar")
        self.button_refresh_address = MyButtonStandard(self.tab_change_address, "Atualizar")
        self.button_search_CEP = MyButtonSearchCEP(self.tab_change_address, self.__cep, self.__street,
                                                   self.__neighborhood, self.__city, self.__state)
        self.button_refresh_personal_data = MyButtonStandard(self.tab_change_personal_data, "Atualizar")
        self.setup_tables_tabs(), self.setup_inputs(), self.setup_buttons()

    def setup_tables_tabs(self):
        self.Table_Changes.setGeometry(QRect(10, 10, 521, 161))
        self.tab_change_address.setFocusPolicy(Qt.TabFocus)
        self.Table_Changes.addTab(self.tab_change_address, "")
        self.Table_Changes.addTab(self.tab_change_personal_data, "")
        self.Table_Changes.setCurrentIndex(0)
        self.Table_Changes.setTabText(self.Table_Changes.indexOf(self.tab_change_address), "Endereços")
        self.Table_Changes.setTabText(self.Table_Changes.indexOf(self.tab_change_personal_data), "Dados Pessoais")

    def setup_inputs(self):
        self.__cep.setGeometry(QRect(10, 10, 191, 31))
        self.__cep.setPlaceholderText('CEP')
        self.__street.setGeometry(QRect(10, 50, 351, 31))
        self.__street.setPlaceholderText('Logradouro')
        self.__home_number.setGeometry(QRect(380, 50, 121, 31))
        self.__home_number.setPlaceholderText('Nº')
        self.__neighborhood.setGeometry(QRect(10, 90, 181, 31))
        self.__neighborhood.setPlaceholderText('Bairro')
        self.__city.setGeometry(QRect(210, 90, 191, 31))
        self.__city.setPlaceholderText('Cidade')
        self.__state.setGeometry(QRect(420, 90, 51, 31))
        self.__state.setPlaceholderText('UF')
        self.__name.setGeometry(QRect(10, 10, 471, 31))
        self.__name.setPlaceholderText('Nome')
        self.__email.setGeometry(QRect(10, 50, 471, 31))
        self.__email.setPlaceholderText('Email')
        self.__phone.setGeometry(QRect(10, 90, 251, 31))
        self.__phone.setPlaceholderText('Telefone')

    def setup_buttons(self):
        self.button_add_address.setGeometry(QRect(420, 10, 75, 31))
        self.button_refresh_address.setGeometry(QRect(340, 10, 75, 31))
        self.button_refresh_personal_data.setGeometry(QRect(400, 90, 75, 31))
        self.button_search_CEP.setGeometry(QRect(210, 10, 51, 31))
        self.button_search_CEP.clicked()

