# -*- coding: utf-8 -*-
from GUI.objects import *
from time import strftime, localtime
from managers import ManagerNewClient, ManagerOperations


class GUIOperationsMain(MyWidgetStandard):
    def __init__(self):
        super().__init__()
        self.change_data_client = None
        self.operations = None
        self.__account = None
        self.setFixedWidth(730)
        self.setFixedHeight(490)
        self.setWindowTitle('Sistema de Cadastro de Clientes')
        self.table_main = QTabWidget(self)
        self.table_operations = QWidget(self)
        self.table_new_customer = QWidget(self)
        self.groupbox_show_customer_operation = QGroupBox(self.table_operations)
        self.groupbox_main_buttons = QGroupBox(self.table_operations)
        self.groupbox_show_new_customer = QGroupBox(self.table_new_customer)
        self.show_customer_display = QTextBrowser(self.groupbox_show_customer_operation)
        self.show_new_customer_display = QTextBrowser(self.groupbox_show_new_customer)
        self.label_search_client = MyLabelStandard(self.table_operations, "Buscar Cliente")
        self.label_birthday = MyLabelStandard(self.table_new_customer, "Data de Nascimento")
        self.label_CPF = MyLabelStandard(self.table_new_customer, "CPF")
        self.label_phone = MyLabelStandard(self.table_new_customer, "Telefone")
        self.label_name = MyLabelStandard(self.table_new_customer, "Nome")
        self.label_email = MyLabelStandard(self.table_new_customer, "Email")
        self.label_CEP = MyLabelStandard(self.table_new_customer, "CEP")
        self.label_street = MyLabelStandard(self.table_new_customer, "Logradouro")
        self.label_number_home = MyLabelStandard(self.table_new_customer, "Nº")
        self.label_neighborhood = MyLabelStandard(self.table_new_customer, "Bairro")
        self.label_city = MyLabelStandard(self.table_new_customer, "Cidade")
        self.label_state = MyLabelStandard(self.table_new_customer, "UF")
        self.label_balance = MyLabelStandard(self.table_new_customer, "Saldo Inicial")
        self.label_credits = MyLabelStandard(self.table_new_customer, "Limite Inicial")
        self.label_top = MyLabelTop(self, "Sistema de Gerenciamento de Cliente")
        self.label_bottom = MyLabelBottom(self, "\u00a9SkyArtur - 2022")
        self.__search = MyInputStandard(self.table_operations)
        self.__birthday = QDateEdit(self.table_new_customer)
        self.__cpf = MyInputCPF(self.table_new_customer)
        self.__phone = MyInputPhone(self.table_new_customer)
        self.__name = MyInputStandard(self.table_new_customer)
        self.__email = MyInputStandard(self.table_new_customer)
        self.__cep = MyInputCEP(self.table_new_customer)
        self.__street = MyInputStandard(self.table_new_customer)
        self.__neighborhood = MyInputStandard(self.table_new_customer)
        self.__city = MyInputStandard(self.table_new_customer)
        self.__state = MyInputStandard(self.table_new_customer)
        self.__home_number = MyInputStandard(self.table_new_customer)
        self.__balance = MyInputFloat(self.table_new_customer)
        self.__credits = MyInputFloat(self.table_new_customer)
        self.__value_operation = MyInputFloat(self.groupbox_main_buttons)
        self.button_deposit = MyButtonStandard(self.groupbox_main_buttons, "Depósito")
        self.button_withdraw = MyButtonStandard(self.groupbox_main_buttons, "Saque")
        self.button_change_credits = MyButtonStandard(self.groupbox_main_buttons, "Alterar Limite")
        self.button_statement = MyButtonStandard(self.groupbox_main_buttons, "Extrato")
        self.button_search = MyButtonStandard(self.table_operations, "Buscar")
        self.button_search_CEP = MyButtonSearchCEP(self.table_new_customer, self.__cep, self.__street,
                                                   self.__neighborhood, self.__city, self.__state)
        self.button_save_new_customer = MyButtonStandard(self.table_new_customer, "Salvar Dados")
        self.button_list_customers = MyButtonStandard(self, "Listar Clientes")
        self.button_show_report = MyButtonStandard(self, "Exibir Relatório")
        self.button_exit = MyButtonStandard(self, "Sair")
        self.radio_name = QRadioButton(self.table_operations)
        self.radio_CPF = QRadioButton(self.table_operations)
        self.radio_account = QRadioButton(self.table_operations)
        self.checkbox_CPF = QCheckBox(self.table_new_customer)
        self.setup_tables(), self.setup_boxes(), self.setup_labels()
        self.setup_radio_buttons(), self.setup_inputs(), self.setup_data_show()
        self.setup_checkboxes(), self.setup_buttons()

    @property
    def return_all_inputs(self):
        my_inputs, data = [
            self.__birthday, self.__cpf, self.__name, self.__email, self.__phone,
            self.__cep, self.__street, self.__home_number, self.__neighborhood,
            self.__city, self.__state, self.__balance, self.__credits
        ], []
        for inputs in my_inputs:
            if inputs.text() is None or inputs.text() == '':
                raise ValueError
            else:
                data.append(inputs.text())
                inputs.clear()
        return tuple(data)

    @property
    def value_operation(self):
        return self.__value_operation.value_input

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value):
        self.__account = value

    def setup_tables(self):
        self.table_main.setGeometry(QRect(10, 60, 711, 361))
        self.table_main.setFont(self.font3)
        self.table_main.setFocusPolicy(Qt.TabFocus)
        self.table_main.setTabPosition(QTabWidget.West)
        self.table_main.setTabShape(QTabWidget.Rounded)
        self.table_main.setElideMode(Qt.ElideNone)
        self.table_operations.setMouseTracking(True)
        self.table_operations.setFocusPolicy(Qt.TabFocus)
        self.table_main.addTab(self.table_operations, "")
        self.table_main.addTab(self.table_new_customer, "")
        self.table_main.setCurrentIndex(0)
        self.table_main.setTabText(self.table_main.indexOf(self.table_operations), "Operações")
        self.table_main.setTabText(self.table_main.indexOf(self.table_new_customer), "Cadastrar Cliente")

    def setup_boxes(self):
        self.groupbox_show_customer_operation.setGeometry(QRect(270, 60, 401, 291))
        self.groupbox_show_customer_operation.setTitle("Dados do Cliente")
        self.groupbox_main_buttons.setGeometry(QRect(10, 60, 251, 291))
        self.groupbox_main_buttons.setTitle("Operações")
        self.groupbox_show_new_customer.setGeometry(QRect(20, 180, 385, 161))
        self.groupbox_show_new_customer.setTitle("")

    def setup_labels(self):
        self.label_search_client.setGeometry(QRect(10, 20, 81, 31))
        self.label_birthday.setGeometry(QRect(20, 20, 111, 31))
        self.label_CPF.setGeometry(QRect(270, 20, 31, 31))
        self.label_phone.setGeometry(QRect(500, 20, 61, 31))
        self.label_name.setGeometry(QRect(20, 60, 41, 31))
        self.label_email.setGeometry(QRect(400, 60, 41, 31))
        self.label_CEP.setGeometry(QRect(20, 100, 41, 31))
        self.label_street.setGeometry(QRect(240, 100, 71, 31))
        self.label_number_home.setGeometry(QRect(575, 100, 31, 31))
        self.label_neighborhood.setGeometry(QRect(20, 140, 49, 31))
        self.label_city.setGeometry(QRect(285, 140, 51, 31))
        self.label_state.setGeometry(QRect(600, 140, 21, 31))
        self.label_balance.setGeometry(QRect(450, 200, 61, 31))
        self.label_credits.setGeometry(QRect(450, 240, 61, 31))
        self.label_top.setGeometry(QRect(10, 9, 711, 41))
        self.label_bottom.setGeometry(QRect(8, 470, 721, 20))

    def setup_inputs(self):
        self.__search.setGeometry(QRect(90, 20, 240, 31))
        self.__birthday.setGeometry(QRect(140, 20, 101, 31))
        self.__birthday.setFont(self.font2)
        self.__birthday.setWrapping(False)
        self.__birthday.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.__birthday.setCalendarPopup(True)
        self.__birthday.setTimeSpec(Qt.LocalTime)
        self.__cpf.setGeometry(QRect(300, 20, 115, 31))
        self.__phone.setGeometry(QRect(550, 20, 115, 31))
        self.__name.setGeometry(QRect(70, 60, 310, 31))
        self.__email.setGeometry(QRect(435, 60, 230, 31))
        self.__cep.setGeometry(QRect(60, 100, 105, 31))
        self.__street.setGeometry(QRect(305, 100, 250, 31))
        self.__home_number.setGeometry(QRect(595, 100, 71, 31))
        self.__neighborhood.setGeometry(QRect(70, 140, 200, 31))
        self.__city.setGeometry(QRect(330, 140, 250, 31))
        self.__state.setGeometry(QRect(625, 140, 41, 31))
        self.__balance.setGeometry(QRect(525, 200, 141, 31))
        self.__balance.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.__credits.setGeometry(QRect(525, 240, 141, 31))
        self.__credits.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.__value_operation.setGeometry(QRect(20, 40, 211, 41))
        self.__value_operation.setPlaceholderText('Digite o Valor da Operação')

    def setup_radio_buttons(self):
        self.radio_account.setGeometry(QRect(350, 20, 71, 31))
        self.radio_account.setText("Nº Conta")
        self.radio_account.setChecked(True)
        self.radio_name.setGeometry(QRect(430, 20, 61, 31))
        self.radio_name.setText("Nome")
        self.radio_CPF.setGeometry(QRect(500, 20, 41, 31))
        self.radio_CPF.setText("CPF")

    def setup_data_show(self):
        self.show_new_customer_display.setGeometry(QRect(10, 10, 375, 141))
        self.show_new_customer_display.setStyleSheet("border: none; padding: 15px;")
        self.show_customer_display.setGeometry(QRect(10, 15, 380, 265))
        self.show_customer_display.setStyleSheet("border: none; padding: 15px;")
        self.show_customer_display.setFont(self.font1)
        self.show_customer_display.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def setup_checkboxes(self):
        self.checkbox_CPF.setGeometry(QRect(420, 20, 95, 31))
        self.checkbox_CPF.setText("Validar?")
        self.checkbox_CPF.clicked.connect(self.check_valid_cpf)

    def setup_buttons(self):
        # ----------------------Button search-----------------------------------
        self.button_search.setGeometry(QRect(560, 20, 111, 31))
        self.button_search.clicked(self.command_search_client)
        # --------------------Button search CEP---------------------------------
        self.button_search_CEP.setGeometry(QRect(170, 100, 51, 31))
        self.button_search_CEP.clicked()
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
        self.button_statement.clicked(self.command_statement)
        # ------------------Button save new client------------------------------
        self.button_save_new_customer.setGeometry(QRect(440, 290, 201, 51))
        self.button_save_new_customer.clicked(self.command_save_new_client)
        # -------------------Button list clients--------------------------------
        self.button_list_customers.setGeometry(QRect(280, 433, 121, 31))
        self.button_list_customers.clicked(self.command_list_clients)
        # --------------------Button show report--------------------------------
        self.button_show_report.setGeometry(QRect(420, 433, 131, 31))
        self.button_show_report.clicked(self.command_show_report)
        # ------------------------Button exit-----------------------------------
        self.button_exit.setGeometry(QRect(570, 433, 131, 31))
        self.button_exit.clicked(self.command_exit_program)

    # ------------------------------------------------------------------------------------------------------------------
    #       COMMANDS
    # ------------------------------------------------------------------------------------------------------------------
    def command_search_client(self):
        if self.__account is not None:
            self.__account = None
        if self.radio_name.isChecked():
            manager = ManagerOperations(name=self.__search.text())
            self.show_customer_display.setText(manager.search_client_by_name())
            self.account = manager.data_client
        elif self.radio_account.isChecked():
            manager = ManagerOperations(num_account=self.__search.text())
            self.show_customer_display.setText(manager.search_client_by_num_account())
            self.account = manager.data_client
        elif self.radio_CPF.isChecked():
            manager = ManagerOperations(cpf=self.__search.text())
            self.show_customer_display.setText(manager.search_client_by_cpf())
            self.account = manager.data_client
        self.__search.clear()

    def command_save_new_client(self):
        try:
            manager = ManagerNewClient(self.return_all_inputs)
            manager.save_new_client()
            self.show_new_customer_display.clear()
            self.show_new_customer_display.setText(manager.report())
            self.show_new_customer_display.setFont(self.font3)
        except ValueError:
            self.show_new_customer_display.setText('DADOS INVÁLIDOS!')
            self.show_new_customer_display.setAlignment(Qt.AlignCenter)
            self.show_new_customer_display.setFont(self.font)

    def command_deposit(self):
        try:
            self.account['balance'] = self.value_operation + self.account['balance']
            self.account['available'] = self.account['balance'] + self.account['credits']
            manager = ManagerOperations()
            manager.data_client = self.account
            manager.data_statement = {
                'id': self.account['id'],
                'date': strftime("%d/%m/%Y", localtime()),
                'op': "deposito",
                "value": f"{self.value_operation:.2f} +"
            }
            manager.update_account()
            self.show_customer_display.setText(manager.print_data_client())
            manager.data_client = None
            manager.data_statement = None
        except ValueError:
            pass
        except TypeError:
            pass
        finally:
            self.__value_operation.clear()
            self.__value_operation.setPlaceholderText('Digite o Valor da Operação')

    def command_withdraw(self):
        try:
            if self.account['available'] < self.value_operation:
                self.__value_operation.setPlaceholderText("Valor indisponível")
                raise ValueError
            self.account['balance'] = self.account['balance'] - self.value_operation
            self.account['available'] = self.account['balance'] + self.account['credits']
            manager = ManagerOperations()
            manager.data_client = self.account
            manager.data_statement = {
                'id': self.account['id'],
                'date': strftime("%d/%m/%Y", localtime()),
                'op': "saque",
                "value": f"{self.value_operation:.2f} -"
            }
            manager.update_account()
            self.show_customer_display.setText(manager.print_data_client())
            manager.data_client = None
            manager.data_statement = None
        except ValueError:
            pass
        except TypeError:
            pass
        finally:
            self.__value_operation.clear()
            self.__value_operation.setPlaceholderText('Digite o Valor da Operação')

    def command_change_credits(self):
        try:
            self.account['credits'] = self.value_operation
            self.account['available'] = self.account['balance'] + self.account['credits']
            manager = ManagerOperations()
            manager.data_client = self.account
            manager.data_statement = {
                'id': self.account['id'],
                'date': strftime("%d/%m/%Y", localtime()),
                'op': "novo limite",
                "value": f"{self.value_operation:.2f}"
            }
            manager.update_account()
            self.show_customer_display.setText(manager.print_data_client())
            manager.data_client = None
            manager.data_statement = None
        except ValueError:
            pass
        except TypeError:
            pass
        finally:
            self.__value_operation.clear()
            self.__value_operation.setPlaceholderText('Digite o Valor da Operação')

    def command_statement(self):
        try:
            manager = ManagerOperations()
            manager.data_client = self.account
            self.show_customer_display.setText(f"{manager.print_data_client()}<br>{manager.display_statement()}")
            manager.data_client = None
            manager.data_statement = None
        except ValueError:
            pass
        except TypeError:
            pass

    def command_list_clients(self):
        if self.account is not None:
            self.account = None
        manager = ManagerOperations()
        self.show_customer_display.setText(
            f"<p><b>Clientes Cadastrados</b></p>"
            f"{manager.print_client_names()}"
        )

    def command_show_report(self):
        if self.account is not None:
            self.account = None
        manager = ManagerOperations()
        self.show_customer_display.setText(f"<b>Relátorio Geral</b><br>{manager.display_report()}")

    def check_valid_cpf(self):
        if self.checkbox_CPF.isChecked():
            if ManagerNewClient.validatorNumberCPF(self.__cpf.text()):
                self.checkbox_CPF.setStyleSheet("""color: #228B22;""")
                self.checkbox_CPF.setText("CPF válido")
            else:
                self.checkbox_CPF.setStyleSheet("""color: red;""")
                self.checkbox_CPF.setText("CPF inválido")
        else:
            self.checkbox_CPF.setStyleSheet("""color: black;""")
            self.checkbox_CPF.setText("Validar?")
