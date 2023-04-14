class Client:

    def __init__(self, full_name, passport_number):

        passport_number = passport_number.replace(" ", "")

        if not passport_number.isdigit() or len(passport_number) != 10:
            raise ValueError("Некорректные данные: номер паспорта должен содержать 10 цифр без пробелов")

        self.full_name = full_name
        self.passport_number = passport_number[:4] + " " + passport_number[4:]
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def close_account(self, account):

        if len(self.accounts) == 1:
            print("Нельзя закрыть единственный счет")
        else:
            remaining_balance = account.balance
            self.accounts.remove(account)
            self.accounts[0].deposit(remaining_balance)

    def get_info(self):

        print("Клиент: " + self.full_name)
        print("Номер паспорта: " + self.passport_number)
        print("Счета:")
        for account in self.accounts:
            print("Номер счета: " + account.account_number)
            print("Баланс: " + str(account.balance))