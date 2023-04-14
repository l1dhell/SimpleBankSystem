class Client
    
    def __init__(self, full_name, passport_number)
        self.full_name = full_name
        self.passport_number = passport_number
        self.accounts = []

    def add_account(self, account)
        self.accounts.append(account)

    def close_account(self, account)
        
        if len(self.accounts) == 1
            print(Нельзя закрыть единственный счет)
        else
            remaining_balance = account.balance
            self.accounts.remove(account)
            self.accounts[0].deposit(remaining_balance)

    def get_info(self)
        
        print(Клиент  + self.full_name)
        print(Номер паспорта  + self.passport_number)
        print(Счета)
        for account in self.accounts
            print(Номер счета  + account.account_number)
            print(Баланс  + str(account.balance))

class Account
    
    def __init__(self, account_number, balance, owner)
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.owner.add_account(self)

    def deposit(self, amount)
        self.balance += amount

    def withdraw(self, amount)
        if amount  self.balance
            print(Недостаточно средств на счете)
        else
            self.balance -= amount

    def transfer(self, amount, recipient)
        if amount  self.balance
            print(Недостаточно средств на счете)
        else
            self.balance -= amount
            recipient.balance += amount

    def get_balance(self)
        return self.balance

client1 = Client(Иванов Иван Иванович, 1234 567890)

account1 = Account(1234567890, 10000, client1)
account2 = Account(0987654321, 5000, client1)

client1.get_info()
