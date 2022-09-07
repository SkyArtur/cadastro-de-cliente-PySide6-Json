from .filer_account import FilerAccount


class FilerClients(FilerAccount):
    def __init__(self):
        super().__init__()

    def define_id_client(self):
        return self.generator_ids('clients')

    def fetch_all_cpfs(self):
        cpfs = [i['cpf'] for i in self.fetch_all_clients()]
        return cpfs

    def fetch_all_names(self):
        names = [i['name'] for i in self.fetch_all_clients()]
        return names

    def save_in_clients(self, data):
        self.save_in("clients", data)

    def fetch_all_clients(self):
        clients = self.fetch_all("clients")
        return clients[1:]
