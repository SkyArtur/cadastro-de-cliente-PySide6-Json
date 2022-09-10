from filer.filer import Filer


class FilerAccount(Filer):
    def __init__(self):
        super().__init__()

    def save_in_account(self, data):
        self.save_in("accounts", data)

    def fetch_all_accounts(self):
        accounts = self.fetch_all("accounts")
        return accounts[1:]

    def save_in_statement(self, data):
        self.save_in("statement", data)

    def fetch_all_statement(self):
        statements = self.fetch_all('statement')
        return statements

    def save_account_where(self, data):
        accounts = self.fetch_all("accounts")
        for i in accounts:
            if data['id'] == i['id']:
                i['balance'] = data['balance']
                i['credits'] = data['credits']
                i['available'] = data['available']
        self.rewrite("accounts", accounts)

