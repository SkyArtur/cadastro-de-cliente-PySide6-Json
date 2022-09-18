import re
from managers.objects import Client
from filer import FilerCustomers
from time import strftime


class ManagerOperations(Client, FilerCustomers):
    def __init__(self, name='default', num_account=None, cpf=None):
        super().__init__()
        self.today = strftime("%d/%m/%Y")
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
        __data = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
        </head>
        <body>
            <div style:"font-family: Arial, Helvetica, sans-serif;">
                <h3 style="text-align: center; background-color: rgb(235, 235, 235);">Dados do Cliente</h3>
                <p><label><b><i>Conta Nº: </i></b><span>{self.data_client['num']}</span></label></p>
                <p><label><b><i>Titular: </i></b><span">{self.data_client['holder'].title()}</span></label></p>
                <p><label><b><i>Saldo: </i></b><span">{self.data_client['balance']:.2f}</span></label></p>
                <p><label><b><i>Limite: </i></b><span">{self.data_client['credits']:.2f}</span></label></p>
                <p><label><b><i>Disponível: </i></b><span>R${self.data_client['available']:.2f}</span></label></p>
            </div>
        </body>
        </html>
        """
        return __data

    def print_client_names(self):
        name = str()
        for names in sorted(self.fetch_all_names()):
            name += f"{names.title()}<br>"
        return name

    def print_report(self):
        report = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
        </head>
        <body>
            <h3 style="text-align: center; height: 50px; background-color: rgb(235, 235, 235);">Relatório Geral</h3>
            <h4>Data: {self.today}</h4>
            <p><b>Número de cliente:</b>  <i>{len(self.fetch_all_customers())}</i></p>
            <p><b>Contas abertas:</b>  <i>{self.sum_num_operations('abertura')}</i></p>
            <p><b>Depósitos realizados:</b>  <i>{self.sum_num_operations('deposito')}</i></p>
            <p><b>Total em depósitos:</b>  R$ <i>{self.sum_value_operations('deposito'):.2f}</i></p>
            <p><b>Saques realizados:</b>  <i>{self.sum_num_operations('saque')}</i></p>
            <p><b>Total em saques:</b>  R$ <i>{self.sum_value_operations('saque'):.2f}</i></p>
            <p><b>Total em contas:</b>  R$ <i>{sum(i['balance'] for i in self.fetch_all_accounts()):.2f}</i></p>
            <p><b>Total em créditos:</b>  R$ <i>{sum(i['credits'] for i in self.fetch_all_accounts()):.2f}</i></p>
        </body>
        </html>
        """
        return report

    def print_statement(self):
        statement = self.fetch_all_statement()
        report = str()
        for stm in statement:
            if stm['id'] == self.data_client['id']:
                report += f"""
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                </head>
                <body>
                    <p style='color: rgb(116, 116, 116); display: flex; justify-content: space-between;'>
                        <span>{stm['date']}</span>
                        <span>{stm['op']}</span>
                        <span style='color: #000;'>R$<i>{stm['value']}</i></span></p>
                </body>
                </html>
                """
        report = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
        </head>
        <body>
            <div style="font-family: Arial, Helvetica, sans-serif;">
                <h3 style="background-color: rgb(235, 235, 235); text-align: center;">Extrato</h3>
            </div>
        </body>
        </html>
        """ + report
        return report

    def search_client_by_name(self):
        data = str()
        if self.name.find(" ") == -1:
            for names in self.fetch_all_customers():
                if names['name'][:names['name'].find(' ')] == self.name:
                    data += f"{names['name']}\n"
        else:
            for name in self.fetch_all_customers():
                if name['name'] == self.name:
                    for accounts in self.fetch_all_accounts():
                        if name['id'] == accounts['id']:
                            self.data_client = accounts
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
            if cpfs['cpf'].replace('.', '').replace('-', '') == self.cpf:
                for accounts in self.fetch_all_accounts():
                    if cpfs['id'] == accounts['id']:
                        self.data_client = accounts
                        data = self.print_data_client()
        return data

    def update_account(self):
        self.save_in_statement(self.data_statement)
        self.save_account_where(self.data_client)

    def sum_num_operations(self, operation):
        return len(
            [
                i['op']
                for i in self.fetch_all_statement()
                if i['op'] == operation and i['date'] == self.today
            ]
        )

    def sum_value_operations(self, operation):
        return sum(
            float(i['value'][:-1].strip())
            for i in self.fetch_all_statement()
            if i['op'] == operation and i['date'] == self.today
        )
