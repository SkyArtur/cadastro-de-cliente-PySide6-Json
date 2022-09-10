from managers.objects import Client, Patterns
from filer import FilerCustomers
from time import strftime, localtime
import re


class ManagerNewClient(Client, FilerCustomers):
    def __init__(self, data: tuple):
        super().__init__()
        if len(data) != 13:
            raise ValueError
        for cpf in data:
            if cpf == '' or cpf is None:
                raise ValueError
        self.id_client = self.define_id_customers()
        self.birthday = data[0]
        self.cpf = data[1]
        self.name = data[2]
        self.email = data[3]
        self.phone = data[4]
        self.cep = data[5]
        self.street = data[6]
        self.home_number = data[7]
        self.neighborhood = data[8]
        self.city = data[9]
        self.state = data[10]
        self.num_account = f"{self.id_client:0>3}-1"
        self.opening = strftime("%d/%m/%Y", localtime())
        self.holder = self.name
        self.balance = float(data[11])
        self.credits = float(data[12])
        for cpf in self.fetch_all_cpfs():
            if self.cpf == cpf:
                raise ValueError
        for name in self.fetch_all_names():
            if self.name == name:
                raise ValueError

    def save_new_client(self):
        self.save_in_customers(
            Patterns.client(
                self.id_client, self.birthday, self.cpf, self.name, self.email, self.phone, self.cep,
                self.street, self.home_number, self.neighborhood, self.city, self.state
            )
        )
        self.save_in_account(
            Patterns.account(
                self.id_client, self.num_account, self.opening, self.holder,
                self.balance, self.credits, self.available
            )
        )
        self.save_in_statement(
            Patterns.statement(
                self.id_client, self.opening, "abertura", self.balance
            )
        )

    def report(self):
        text = f"""<p><b>Novo Cliente Cadastrado com Sucesso</b></p>
        <p><b>Data de Nascimento:</b> {self.birthday}</p>
        <p><b>Nome:</b> {self.name.title()} <b>CPF:</b> {self.cpf}</p>
        <p><b>Telefone:</b> {self.phone} <b>Email:</b> {self.email}</p>
        <p><b>Logradouro:</b> {self.street.title()} <b>Nº</b> {self.home_number}</p>      
        <p><b>CEP:</b> {self.cep}</p>
        <p><b>Bairro:</b> {self.neighborhood.title()} <b>Cidade:</b> {self.city.title()} <b>UF:</b> {self.state}</p>
        <p><b>Limite Inicial:</b> R${self.credits:.2f} <b>Saldo Inicial:</b> R${self.balance:.2f}</p>
        <p><b>Disponível:</b> R${self.available:.2f}</p>"""
        return text

    @staticmethod
    def validatorNumberCPF(cpf: str):
        digit1, digit2 = 0, 0
        try:
            patt = re.search("^([0-9]{3}).?([0-9]{3}).?([0-9]{3})-?([0-9]{2})$", cpf)
            __cpf = f"{patt.group(1)}{patt.group(2)}{patt.group(3)}{patt.group(4)}"
        except AttributeError:
            return False
        for index, factor in enumerate(range(10, 1, -1)):
            digit1 += int(__cpf[index]) * factor
        for index, factor in enumerate(range(11, 1, -1)):
            digit2 += int(__cpf[index]) * factor
        digit1 = 11 - (digit1 % 11)
        digit2 = 11 - (digit2 % 11)
        digit1 = 0 if digit1 > 9 else digit1
        digit2 = 0 if digit2 > 9 else digit2
        return f"{digit1}{digit2}" == patt.group(4)