from os import path, mkdir
from .models import *
import json


class Filer:
    file = [
        "./storage/users.json",
        "./storage/clients.json",
        "./storage/accounts.json",
        "./storage/statement.json"
    ]
    patterns = [users, clients, account, statement]

    def __init__(self):
        self.__setup_files()

    def __setup_files(self):
        if not path.exists("./storage"):
            mkdir("./storage")
        for i in range(4):
            if not path.exists(self.file[i]):
                with open(self.file[i], 'w') as file:
                    json.dump(self.patterns[i], file, indent=4, ensure_ascii=False)
        return

    def __select_table(self, table: str):
        tabs = ['users', 'clients', 'accounts', 'statement']
        index = None
        for i in range(len(tabs)):
            if tabs[i] == table:
                index = i
        return self.file[index]

    def fetch_all(self, table: str):
        with open(self.__select_table(table)) as file:
            data = json.load(file)
        return data

    def save_in(self, table: str, data: dict):
        __data = self.fetch_all(table)
        __data.append(data)
        with open(self.__select_table(table), 'w') as file:
            json.dump(__data, file, indent=4, ensure_ascii=False)

    def generator_ids(self, table: str):
        return int(len(self.fetch_all(table)))
