
class User:

    def __init__(self):
        self.__id = None
        self.__name = None
        self.__username = None
        self.__password = None
        self.__password_confirm = None
        self.__data = None

    @property
    def id_user(self):
        return self.__id

    @id_user.setter
    def id_user(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def password_confirm(self):
        return self.__password_confirm

    @password_confirm.setter
    def password_confirm(self, value):
        self.__password_confirm = value


