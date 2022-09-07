class Address:
    def __init__(self):
        self.__cep = None
        self.__street = None
        self.__home_number = None
        self.__neighborhood = None
        self.__city = None
        self.__state = None

    @property
    def cep(self):
        return self.__cep

    @cep.setter
    def cep(self, value):
        self.__cep = value

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value.lower()

    @property
    def home_number(self):
        return self.__home_number

    @home_number.setter
    def home_number(self, value):
        self.__home_number = value

    @property
    def neighborhood(self):
        return self.__neighborhood

    @neighborhood.setter
    def neighborhood(self, value):
        self.__neighborhood = value.lower()

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value.lower()

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value):
        self.__state = value.lower()
