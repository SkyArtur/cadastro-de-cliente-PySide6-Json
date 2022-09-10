from os import path, mkdir
from filer.models import *
import json


class Filer:
    file = [
        "./storage/users.json",
        "./storage/customers.json",
        "./storage/accounts.json",
        "./storage/statement.json"
    ]
    model = [users, customers, account, statement]

    def __init__(self):
        self.__setup_files()

    def __setup_files(self):
        if not path.exists("./storage"):
            mkdir("./storage")
        for i in range(4):
            if not path.exists(self.file[i]):
                with open(self.file[i], 'w') as file:
                    json.dump(self.model[i], file, indent=4, ensure_ascii=False)
        return

    def __select_file(self, target_file: str):
        mods, index = ['users', 'customers', 'accounts', 'statement'], None
        for i in range(len(mods)):
            if mods[i] == target_file:
                index = i
        return self.file[index]

    def fetch_all(self, target_file: str):
        with open(self.__select_file(target_file)) as file:
            data_list = json.load(file)
        return data_list

    def rewrite(self, target_file: str, data):
        with open(self.__select_file(target_file), 'w') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def save_in(self, target_file: str, data: dict):
        file_data = self.fetch_all(target_file)
        file_data.append(data)
        with open(self.__select_file(target_file), 'w') as file:
            json.dump(file_data, file, indent=4, ensure_ascii=False)

    def generator_ids(self, target_file: str):
        return len(self.fetch_all(target_file))
