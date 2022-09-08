from managers.objects.statement import Statement


class Account(Statement):
    def __init__(self):
        super().__init__()
        self.opening = self.date
        self.__num_account = None
        self.__holder = None
        self.__balance = None
        self.__credits = None

    @property
    def num_account(self):
        return self.__num_account

    @num_account.setter
    def num_account(self, value):
        self.__num_account = value

    @property
    def holder(self):
        return self.__holder

    @holder.setter
    def holder(self, value):
        self.__holder = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    @property
    def credits(self):
        return self.__credits

    @credits.setter
    def credits(self, value):
        self.__credits = value

    @property
    def available(self):
        return self.balance + self.credits

    def draft(self, value):
        if self.available >= value:
            self.balance -= value
        else:
            raise ValueError

    def deposit(self, value):
        self.balance += value
