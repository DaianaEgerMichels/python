class Account:

    def __init__(self, number, owner, balance, limit):
        print("Building the object... {}".format(self))
        self.number = number
        self.owner = owner
        self.balance = balance
        self.limit = limit


    def generate_extract(self):
        print("The balance of this account is {}, owner {}".format(self.balance, self.owner))
    def to_deposit(self, value):
        self.balance += value
    def to_withdraw(self, value):
        self.balance -= value
