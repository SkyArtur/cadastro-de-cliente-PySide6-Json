from filer import FilerUser
from .objects import User


class ManagerLogin(User, FilerUser):
    def __init__(self):
        super().__init__()

    def valid_password(self, name, password):
        for i in self.fetch_all_users():
            if name == i['username'] and password == i['password']:
                return True
        return False


class ManagerNewUser(ManagerLogin):
    def __init__(self, *args):
        super().__init__()
        self.id_user = self.generator_id_users()
        self.name = args[0]
        self.username = args[1]
        self.password = args[2]
        self.password_confirm = args[3]

    def valid_username(self):
        if self.username == "" or self.username is None:
            return False
        for i in self.fetch_all_usernames():
            if self.username == i:
                return False
        return True

    def confirm_password(self):
        if self.password == "" or self.password is None:
            return False
        return self.password == self.password_confirm

    def save_new_user(self):
        user = {
            "id": self.id_user,
            "name": self.name,
            "username": self.username,
            "password": self.password
        }
        self.save_in_users(user)
