class ManagerNewClient:
    def __init__(self, data: dict):
        for i in data.values():
            if i == '' or i is None:
                raise ValueError
        self.birthday = data['birthday']
        self.name = data['name']
        self.cpf = data['cpf']
        self.phone = data['phone']
        self.email = data['email']
        self.cep = data['cep']
        self.street = data['street']
        self.home_number = data['home_number']
        self.neighborhood = data['neighborhood']
        self.city = data['city']
        self.state = data['state']
        self.balance = data['balance']
        self.credits = data['credits']

    def report(self):
        text = f"Data de Nascimento: {self.birthday}\n" \
               f"Nome: {self.name}      CPF: {self.cpf}\n" \
               f"Telefone: {self.phone}      Email: {self.email}\n" \
               f"Logradouro: {self.street}  Nº{self.home_number}      CEP: {self.cep}\n" \
               f"Bairro: {self.neighborhood}      Cidade: {self.city}      UF: {self.state}\n" \
               f"Limite Inicial: R${self.credits:.2f}      Saldo Inicial: R${self.balance:.2f}\n" \
               f"Disponível: R${self.credits + self.balance}"
        return text