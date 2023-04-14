from client import Client
from account import Account

client1 = Client("Иванов Иван Иванович", "1234 567890")

account1 = Account("1234567890", 10000, client1)
account2 = Account("0987654321", 5000, client1)

client1.get_info()