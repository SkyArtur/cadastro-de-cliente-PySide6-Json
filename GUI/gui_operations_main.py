# -*- coding: utf-8 -*-
from .objects import *
from .gui_operations_account import GUIOperationsAccount
from .gui_operations_data_client import GUIOperationsDataClient
from managers import ManagerNewClient


class GUIOperationsMain(MyWidgetStandard):
    def __init__(self):
        super().__init__()
        self.change_data_client = None
        self.operations = None
        self.setFixedWidth(830)
        self.setFixedHeight(490)
        self.setWindowTitle('Sistema de Cadastro de Clientes')
        self.table_main = QTabWidget(self)
        self.table_operations = QWidget(self)
        self.table_new_client = QWidget(self)
        self.groupbox_data_show_client_operation = QGroupBox(self.table_operations)
        self.groupbox_main_buttons = QGroupBox(self.table_operations)
        self.groupbox_data_show_new_client = QGroupBox(self.table_new_client)
        self.data_show_new_client_display = QTextBrowser(self.groupbox_data_show_new_client)
        self.data_show_client_display = QTextBrowser(self.groupbox_data_show_client_operation)
        self.label_search_client = MyLabelStandard(self.table_operations, "Buscar Cliente")
        self.label_birthday = MyLabelStandard(self.table_new_client, "Data de Nascimento")
        self.label_CPF = MyLabelStandard(self.table_new_client, "CPF")
        self.label_phone = MyLabelStandard(self.table_new_client, "Telefone")
        self.label_name = MyLabelStandard(self.table_new_client, "Nome")
        self.label_email = MyLabelStandard(self.table_new_client, "Email")
        self.label_CEP = MyLabelStandard(self.table_new_client, "CEP")
        self.label_street = MyLabelStandard(self.table_new_client, "Logradouro")
        self.label_number_home = MyLabelStandard(self.table_new_client, "Nº")
        self.label_neighborhood = MyLabelStandard(self.table_new_client, "Bairro")
        self.label_city = MyLabelStandard(self.table_new_client, "Cidade")
        self.label_state = MyLabelStandard(self.table_new_client, "UF")
        self.label_balance = MyLabelStandard(self.table_new_client, "Saldo Inicial")
        self.label_credits = MyLabelStandard(self.table_new_client, "Limite Inicial")
        self.label_top = MyLabelTop(self, "Sistema de Gerenciamento de Cliente")
        self.label_bottom = MyLabelBottom(self, "\u00a9SkyArtur - 2022")
        self.__search = MyInputStandard(self.table_operations)
        self.__birthday = QDateEdit(self.table_new_client)
        self.__cpf = MyInputCPF(self.table_new_client)
        self.__phone = MyInputStandard(self.table_new_client)
        self.__name = MyInputStandard(self.table_new_client)
        self.__email = MyInputStandard(self.table_new_client)
        self.__cep = MyInputCEP(self.table_new_client)
        self.__street = MyInputStandard(self.table_new_client)
        self.__neighborhood = MyInputStandard(self.table_new_client)
        self.__city = MyInputStandard(self.table_new_client)
        self.__state = MyInputStandard(self.table_new_client)
        self.__home_number = MyInputStandard(self.table_new_client)
        self.__balance = MyInputFloat(self.table_new_client)
        self.__credits = MyInputFloat(self.table_new_client)
        self.button_deposit = MyButtonStandard(self.groupbox_main_buttons, "Depósito")
        self.button_withdraw = MyButtonStandard(self.groupbox_main_buttons, "Saque")
        self.button_change_credits = MyButtonStandard(self.groupbox_main_buttons, "Alterar Limite")
        self.button_statement = MyButtonStandard(self.groupbox_main_buttons, "Extrato")
        self.button_change_data_client = MyButtonStandard(self.groupbox_main_buttons, "Alterar Dados Pessoais")
        self.button_search = MyButtonStandard(self.table_operations, "Buscar")
        self.button_search_CEP = MyButtonSearchCEP(self.table_new_client, self.__cep,
                                                   self.__street, self.__neighborhood, self.__city, self.__state)
        self.button_save_new_client = MyButtonStandard(self.table_new_client, "Salvar Dados")
        self.button_list_clients = MyButtonStandard(self, "Listar Clientes")
        self.button_show_report = MyButtonStandard(self, "Exibir Relatório")
        self.button_exit = MyButtonStandard(self, "Sair")
        self.radio_name_client = QRadioButton(self.table_operations)
        self.radio_CPF = QRadioButton(self.table_operations)
        self.radio_num_account = QRadioButton(self.table_operations)
        self.checkbox_CPF = QCheckBox(self.table_new_client)
        self.setup_tables(), self.setup_boxes(), self.setup_labels()
        self.setup_radio_buttons(), self.setup_inputs(), self.setup_data_show()
        self.setup_checkboxes(), self.setup_buttons()

    @property
    def all(self):
        data = {
            "birthday": self.__birthday.text(),
            "cpf": self.__cpf,
            "phone": self.__phone,
            "name": self.__name,
            "email": self.__email,
            "cep": self.__cep,
            "street": self.__street,
            "home_number": self.__home_number,
            "neighborhood": self.__neighborhood,
            "city": self.__city,
            "state": self.__state,
            "balance": self.__balance,
            "credits": self.__credits
        }
        for i in data.values():
            if i is None or i == '':
                raise ValueError
        return data

    def setup_tables(self):
        self.table_main.setGeometry(QRect(10, 60, 811, 361))
        self.table_main.setFont(self.font2)
        self.table_main.setFocusPolicy(Qt.TabFocus)
        self.table_main.setTabPosition(QTabWidget.West)
        self.table_main.setTabShape(QTabWidget.Rounded)
        self.table_main.setElideMode(Qt.ElideNone)
        self.table_operations.setObjectName(u"table_operations")
        self.table_operations.setMouseTracking(True)
        self.table_operations.setFocusPolicy(Qt.TabFocus)
        self.table_main.addTab(self.table_operations, "")
        self.table_main.addTab(self.table_new_client, "")
        self.table_main.setCurrentIndex(0)
        self.table_main.setTabText(self.table_main.indexOf(self.table_operations), "Operações")
        self.table_main.setTabText(self.table_main.indexOf(self.table_new_client), "Cadastrar Cliente")

    def setup_boxes(self):
        self.groupbox_data_show_client_operation.setGeometry(QRect(270, 60, 501, 291))
        self.groupbox_data_show_client_operation.setTitle("Dados do Cliente")
        self.groupbox_main_buttons.setGeometry(QRect(10, 60, 251, 291))
        self.groupbox_main_buttons.setTitle("Operações")
        self.groupbox_data_show_new_client.setGeometry(QRect(20, 180, 461, 161))
        self.groupbox_data_show_new_client.setTitle("")

    def setup_labels(self):
        self.label_search_client.setGeometry(QRect(10, 20, 81, 31))
        self.label_birthday.setGeometry(QRect(20, 20, 111, 31))
        self.label_CPF.setGeometry(QRect(270, 20, 31, 31))
        self.label_phone.setGeometry(QRect(570, 20, 61, 31))
        self.label_name.setGeometry(QRect(20, 60, 41, 31))
        self.label_email.setGeometry(QRect(470, 60, 41, 31))
        self.label_CEP.setGeometry(QRect(20, 100, 41, 31))
        self.label_street.setGeometry(QRect(300, 100, 71, 31))
        self.label_number_home.setGeometry(QRect(670, 100, 31, 31))
        self.label_neighborhood.setGeometry(QRect(20, 140, 49, 31))
        self.label_city.setGeometry(QRect(350, 140, 51, 31))
        self.label_state.setGeometry(QRect(700, 140, 21, 31))
        self.label_balance.setGeometry(QRect(510, 200, 61, 31))
        self.label_credits.setGeometry(QRect(510, 240, 61, 31))
        self.label_top.setGeometry(QRect(10, 9, 811, 41))
        self.label_bottom.setGeometry(QRect(8, 470, 821, 20))

    def setup_inputs(self):
        self.__search.setGeometry(QRect(90, 20, 341, 31))
        self.__birthday.setGeometry(QRect(140, 20, 101, 31))
        self.__birthday.setFont(self.font1)
        self.__birthday.setWrapping(False)
        self.__birthday.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.__birthday.setCalendarPopup(True)
        self.__birthday.setTimeSpec(Qt.LocalTime)
        self.__cpf.setGeometry(QRect(300, 20, 141, 31))
        self.__phone.setGeometry(QRect(630, 20, 141, 31))
        self.__name.setGeometry(QRect(70, 60, 371, 31))
        self.__email.setGeometry(QRect(510, 60, 261, 31))
        self.__cep.setGeometry(QRect(60, 100, 121, 31))
        self.__street.setGeometry(QRect(370, 100, 281, 31))
        self.__home_number.setGeometry(QRect(700, 100, 71, 31))
        self.__neighborhood.setGeometry(QRect(70, 140, 251, 31))
        self.__city.setGeometry(QRect(400, 140, 271, 31))
        self.__state.setGeometry(QRect(730, 140, 41, 31))
        self.__balance.setGeometry(QRect(590, 200, 141, 31))
        self.__balance.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.__credits.setGeometry(QRect(590, 240, 141, 31))
        self.__credits.setInputMethodHints(Qt.ImhFormattedNumbersOnly)

    def setup_radio_buttons(self):
        self.radio_name_client.setGeometry(QRect(530, 20, 61, 31))
        self.radio_name_client.setText("Nome")
        self.radio_CPF.setGeometry(QRect(600, 20, 41, 31))
        self.radio_CPF.setText("CPF")
        self.radio_num_account.setGeometry(QRect(450, 20, 71, 31))
        self.radio_num_account.setText("Nº Conta")
        self.radio_num_account.setChecked(True)

    def setup_data_show(self):
        self.data_show_new_client_display.setGeometry(QRect(10, 10, 441, 141))
        self.data_show_new_client_display.setStyleSheet("border: none; padding: 15px;")
        self.data_show_client_display.setGeometry(QRect(10, 15, 480, 265))
        self.data_show_client_display.setStyleSheet("border: none; padding: 15px;")

    def setup_checkboxes(self):
        self.checkbox_CPF.setGeometry(QRect(450, 20, 75, 31))
        self.checkbox_CPF.setText("Validar?")

    def setup_buttons(self):
        # ----------------------Button search-----------------------------------
        self.button_search.setGeometry(QRect(660, 20, 111, 31))
        # --------------------Button search CEP---------------------------------
        self.button_search_CEP.setGeometry(QRect(190, 100, 51, 31))
        self.button_search_CEP.clicked()
        # -----------------Button change data client----------------------------
        self.button_change_data_client.setGeometry(QRect(20, 40, 211, 41))
        self.button_change_data_client.clicked(self.command_change_data_client)
        # ----------------------Button deposit----------------------------------
        self.button_deposit.setGeometry(QRect(20, 90, 211, 41))
        self.button_deposit.clicked(self.command_deposit)
        # ---------------------Button withdraw----------------------------------
        self.button_withdraw.setGeometry(QRect(20, 140, 211, 41))
        self.button_withdraw.clicked(self.command_withdraw)
        # ------------------Button change credits-------------------------------
        self.button_change_credits.setGeometry(QRect(20, 190, 211, 41))
        self.button_change_credits.clicked(self.command_change_credits)
        # --------------------Button statement----------------------------------
        self.button_statement.setGeometry(QRect(20, 240, 211, 41))
        # ------------------Button save new client------------------------------
        self.button_save_new_client.setGeometry(QRect(534, 290, 201, 51))
        self.button_save_new_client.clicked(self.command_save_new_client)
        # -------------------Button list clients--------------------------------
        self.button_list_clients.setGeometry(QRect(380, 433, 121, 31))
        # --------------------Button show report--------------------------------
        self.button_show_report.setGeometry(QRect(520, 433, 131, 31))
        # ------------------------Button exit-----------------------------------
        self.button_exit.setGeometry(QRect(670, 433, 131, 31))
        self.button_exit.clicked(self.command_exit_program)

    # ------------------------------------------------------------------------------------------------------------------
    #       COMMANDS
    # ------------------------------------------------------------------------------------------------------------------
    def command_save_new_client(self):
        try:
            data = ManagerNewClient(self.all)
            self.data_show_new_client_display.setText(data.report())
            self.data_show_new_client_display.setFont(self.font2)
        except TypeError:
            self.data_show_new_client_display.setText('DADOS INVÁLIDOS!')
            self.data_show_new_client_display.setAlignment(Qt.AlignCenter)
            self.data_show_new_client_display.setFont(self.font)

    def command_change_data_client(self):
        self.change_data_client = GUIOperationsDataClient()
        self.change_data_client.show()

    def command_deposit(self):
        self.operations = GUIOperationsAccount("Depósito")
        self.operations.show()

    def command_withdraw(self):
        self.operations = GUIOperationsAccount("Saque")
        self.operations.show()

    def command_change_credits(self):
        self.operations = GUIOperationsAccount("Alterar Limite")
        self.operations.show()
