from time import strftime


class Statement:
    def __init__(self):
        self.date = strftime('%d/%m/%Y')
        self.__operation = None
        self.__value = None

    @property
    def operation(self):
        return self.__operation

    @operation.setter
    def operation(self, value):
        self.__operation = value

    @property
    def value_operation(self):
        return self.__value

    @value_operation.setter
    def value_operation(self, value):
        self.__value = value
