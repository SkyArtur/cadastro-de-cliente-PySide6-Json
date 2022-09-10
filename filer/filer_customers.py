from filer.filer_account import FilerAccount


class FilerCustomers(FilerAccount):
    def __init__(self):
        super().__init__()

    def define_id_customers(self):
        return self.generator_ids('customers')

    def fetch_all_cpfs(self):
        cpfs = [i['cpf'] for i in self.fetch_all_customers()]
        return cpfs

    def fetch_all_names(self):
        names = [i['name'] for i in self.fetch_all_customers()]
        return names

    def save_in_customers(self, data):
        self.save_in("customers", data)

    def fetch_all_customers(self):
        clients = self.fetch_all("customers")
        return clients[1:]
