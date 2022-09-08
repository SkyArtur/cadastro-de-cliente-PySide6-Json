from managers.objects import Client
from filer import FilerCustomers
from time import strftime, localtime


class ManagerOperations(Client, FilerCustomers):
    def __init__(self, name='default', num_account=None, cpf=None):
        super().__init__()
        self.__date = strftime("%d/%m/%Y")
        self.name = name
        self.cpf = cpf
        self.num_account = num_account
        self.__data_client = None
        self.__data_statement = None

    @property
    def data_client(self):
        return self.__data_client

    @data_client.setter
    def data_client(self, value: dict):
        self.__data_client = value

    @property
    def data_statement(self):
        return self.__data_statement

    @data_statement.setter
    def data_statement(self, value):
        self.__data_statement = value

    def print_data_client(self):
        __data = f"<b>Conta Nº:</b> {self.data_client['num']}<br>" \
                 f"<b>Titular:</b> {self.data_client['holder'].title()}<br>" \
                 f"<b>Saldo:</b> R${self.data_client['balance']:.2f}<br>" \
                 f"<b>Limite:</b> R${self.data_client['credits']:.2f}<br>" \
                 f"<b>Total Disponível:</b> R${self.data_client['available']:.2f}"
        return __data

    def print_client_names(self):
        __name = str()
        for i in self.fetch_all_names():
            __name += f"{i.title()}<br>"
        return __name

    def search_client_by_name(self):
        data = str()
        if self.name.find(" ") == -1:
            for names in self.fetch_all_customers():
                if names['name'][:names['name'].find(' ')] == self.name:
                    data += f"{names['name']}\n"
        else:
            for name in self.fetch_all_customers():
                if name['name'] == self.name:
                    for account in self.fetch_all_accounts():
                        if name['id'] == account['id']:
                            self.data_client = account
                            data = self.print_data_client()
        return data

    def search_client_by_num_account(self):
        data = str()
        for accounts in self.fetch_all_accounts():
            if accounts['num'] == self.num_account:
                self.data_client = accounts
                data = self.print_data_client()
        return data

    def search_client_by_cpf(self):
        data = str()
        for cpfs in self.fetch_all_customers():
            if cpfs['cpf'] == self.cpf:
                for accounts in self.fetch_all_accounts():
                    if cpfs['id'] == accounts['id']:
                        self.data_client = accounts
                        data = self.print_data_client()
        return data

    def update_account(self):
        self.save_in_statement(self.data_statement)
        self.save_account_where(self.data_client)

    def display_statement(self):
        statement = self.fetch_all_statement()
        report = ""
        for stm in statement:
            if stm['id'] == self.data_client['id']:
                report += f"<p>{stm['date']} | {stm['op']} == <b>{stm['value']}</b></p>"
        report = f"<b>Data</b> ------ <b>Operação</b> ------ <b>Valor</b>" + report
        return report

    def sum_num_operations(self, operation):
        return len(
            [
                i['op']
                for i in self.fetch_all_statement()
                if i['op'] == operation and i["date"] == self.__date
            ]
        )

    def sum_value_operations(self, operation):
        return sum(
            float(i['value'][:-1].strip())
            for i in self.fetch_all_statement()
            if i['op'] == operation and i['date'] == self.__date
        )

    def display_report(self):
        report = f"Data: {self.__date}<br>"\
                 f"Número de cliente: <b>{len(self.fetch_all_customers())}</b><br>" \
                 f"Contas abertas: <b>{self.sum_num_operations('abertura')}</b><br>" \
                 f"Depósitos realizados: <b>{self.sum_num_operations('deposito')}</b><br>" \
                 f"Total em depósitos: R$ <b>{self.sum_value_operations('deposito'):.2f}</b><br>" \
                 f"Saques realizados: <b>{self.sum_num_operations('saque')}</b><br>" \
                 f"Total em saques: R$ <b>{self.sum_value_operations('saque'):.2f}</b><br><br>" \
                 f"Total em contas: R$ <b>{sum(i['balance'] for i in self.fetch_all_accounts()):.2f}</b><br>" \
                 f"Total em créditos: R$ <b>{sum(i['credits'] for i in self.fetch_all_accounts()):.2f}</b><br>"
        return report
