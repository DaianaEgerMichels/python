def create_account(number, owner_account, balance, limit):
    account = {"number": number, "owner_account": owner_account, "balance": balance, "limit": limit}
    return account

def to_deposit(account, value):
    account["balance"] += value
def to_withdraw(account, value):
    account["balance"] -= value
def generate_extract(account):
    print("Balance {}".format(account["balance"]))