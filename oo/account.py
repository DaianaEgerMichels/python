class Account:

    def __init__(self, number, owner, balance, limit):
        print("Building the object... {}".format(self))
        self.__number = number
        self.__owner = owner
        self.__balance = balance
        self.__limit = limit


    def generate_extract(self):
        print("The balance of this account is {}, owner {}".format(self.__balance, self.__owner))
    def to_deposit(self, value):
        self.__balance += value
    def to_withdraw(self, value):
        self.__balance -= value

    def to_transfer(self, value, destiny):
        self.to_withdraw(value)
        destiny.to_deposit(value)

