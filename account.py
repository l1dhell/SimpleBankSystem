class Account:
    accounts = []

    def __init__(self, account_number, balance, owner):

        if len(account_number) != 10:
            raise ValueError("Номер счета должен содержать 10 символов")

        for account in Account.accounts:
            if account.account_number == account_number:
                raise ValueError("Номер счета уже существует")

        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.owner.add_account(self)
        Account.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств на счете")
        else:
            self.balance -= amount

    def transfer(self, amount, recipient):
        if amount > self.balance:
            print("Недостаточно средств на счете")
        else:
            self.balance -= amount
            recipient.balance += amount

    def get_balance(self):
        return self.balance