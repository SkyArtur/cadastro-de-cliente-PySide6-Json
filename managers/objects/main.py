from time import strftime
from dataclasses import dataclass


@dataclass
class Statement:
    date = strftime('%d/%m/%Y')
    operation = None
    value_operation = None


@dataclass
class Account(Statement):
    num_account = None
    holder = None
    balance = None
    credits = None

    def __post_init(self):
        super().__init__()
        self.opening = self.date

    @property
    def available(self):
        return self.balance + self.credits


@dataclass
class Address:
    cep = None
    street = None
    home_number = None
    neighborhood = None
    city = None
    state = None


@dataclass
class Client(Account, Address):
    id_client = None
    birthday = None
    cpf = None
    name = None
    email = None
    phone = None
