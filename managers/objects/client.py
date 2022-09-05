from .address import Address
from .account import Account


class Client(Account, Address):
    def __init__(self):
        super().__init__()
        self.__id = None
        self.__birthday = None
        self.__cpf = None
        self.__name = None
        self.__email = None
        self.__phone = None

    @property
    def id_client(self):
        return self.__id

    @id_client.setter
    def id_client(self, value):
        self.__id = value

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):
        self.__birthday = value

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, value):
        self.__cpf = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value.lower()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value.lower()

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__phone = value
