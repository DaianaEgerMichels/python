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

    def get_balance(self):
        return self.__balance

    def get_owner(self):
        return self.__owner

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit

    @staticmethod
    def bank_code():
        return "001"

    @staticmethod
    def banks_codes():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}