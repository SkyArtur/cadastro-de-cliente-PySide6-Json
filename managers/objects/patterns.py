class Patterns:
    @staticmethod
    def user(*args):
        user = {
            "id": args[0],
            "name": args[1],
            "username": args[2],
            "password": args[3]
        }
        return user

    @staticmethod
    def client(*args):
        client = {
            "id": args[0],
            "birthday": args[1],
            "cpf": args[2],
            "name": args[3],
            "email": args[4],
            "phone": args[5],
            "cep": args[6],
            "street": args[7],
            "number": args[8],
            "neighborhood": args[9],
            "city": args[10],
            "state": args[11]
        }
        return client

    @staticmethod
    def account(*args):
        account = {
            "id": args[0],
            "num": args[1],
            "opening": args[2],
            "holder": args[3],
            "balance": args[4],
            "credits": args[5],
            "available": args[6]
        }
        return account

    @staticmethod
    def statement(*args):
        statement = {
            "id": args[0],
            "date": args[1],
            "op": args[2],
            "value": args[3]
        }
        return statement
