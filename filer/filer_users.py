from filer.filer import Filer


class FilerUser(Filer):
    def __init__(self):
        super().__init__()

    def generator_id_users(self):
        return self.generator_ids("users")

    def save_in_users(self, data):
        self.save_in("users", data)

    def fetch_all_users(self):
        users = self.fetch_all("users")
        return users

    def fetch_all_names(self):
        names = [i['name'] for i in self.fetch_all_users()]
        return names[1:]

    def fetch_all_usernames(self):
        username = [i['username'] for i in self.fetch_all_users()]
        return username[1:]

    def fetch_all_password(self):
        password = [i['password'] for i in self.fetch_all_users()]
        return password[1:]

