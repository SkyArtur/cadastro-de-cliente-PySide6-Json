from filer import FilerUser
from managers.objects import User, Patterns


class ManagerLogin(User, FilerUser):
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password

    def valid_password(self):
        for dicts in self.fetch_all_users():
            if self.username == dicts['username'] and self.password == dicts['password']:
                return True
        return False


class ManagerNewUser(User, FilerUser):
    def __init__(self, name, username, password, confirm):
        super().__init__()
        self.name = name
        self.username = username
        self.password = password
        self.password_confirm = confirm

    def valid_username(self):
        if self.username == "" or self.username is None:
            return False
        for names in self.fetch_all_usernames():
            if self.username == names:
                return False
        return True

    def confirm_password(self):
        if self.password == "" or self.password is None:
            return False
        return self.password == self.password_confirm

    def save_new_user(self):
        self.save_in_users(
            Patterns.user(
                id=self.generator_id_users(),
                name=self.name,
                username=self.username,
                password=self.password
            )
        )
