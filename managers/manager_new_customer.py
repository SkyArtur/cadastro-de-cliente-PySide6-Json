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
                id=self.id_client,
                birthday=self.birthday,
                cpf=self.cpf,
                name=self.name.lower(),
                email=self.email,
                phone=self.phone,
                cep=self.cep,
                street=self.street.lower(),
                number=self.home_number,
                neighborhhood=self.neighborhood.lower(),
                city=self.city.lower(),
                state=self.state
            )
        )
        self.save_in_account(
            Patterns.account(
                id=self.id_client,
                num=self.num_account,
                opening=self.opening,
                hplder=self.holder.lower(),
                balance=self.balance,
                credits=self.credits,
                availabel=self.available
            )
        )
        self.save_in_statement(
            Patterns.statement(
                id=self.id_client,
                date=self.opening,
                op="abertura",
                value=self.balance
            )
        )

    def report(self):
        text = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
        </head>
        <body>
            <h3 style="text-align: center;"><b>Novo Cliente Cadastrado com Sucesso</b></h3>
            <p><b>Data de Nascimento:</b> <i>{self.birthday}</i></p>
            <p><b>Nome:</b> <i>{self.name.title()}</i>  <b>CPF:</b> <i>{self.cpf}</i></p>
            <p><b>Telefone:</b> <i>{self.phone}</i>  <b>Email:</b> <i>{self.email}</i></p>
            <p><b>Logradouro:</b> <i>{self.street.title()}</i>  <b>Nº</b> <i>{self.home_number}</i></p>      
            <p><b>CEP:</b> <i><i></i></i></p>
            <p><b>Bairro:</b> <i>{self.neighborhood.title()}</i> <b>Cidade:</b> <i>{self.city.title()}</i> <b>UF:</b> <i>{self.state}</i></p>
            <p><b>Limite Inicial:</b> R$<i>{self.credits:.2f}</i> <b>Saldo Inicial:</b> R$<i>{self.balance:.2f}</i></p>
            <p><b>Disponível:</b> R$<i>{self.available:.2f}<</i>/p>
        </body>
        </html>
        """
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
