class Account:

    def __init__(self, number, owner, balance, limit):
        print("Building the object... {}".format(self))
        self.number = number
        self.owner = owner
        self.balance = balance
        self.limit = limit

