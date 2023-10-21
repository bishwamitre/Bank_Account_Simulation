# Account class
# Errors indicated by "raise" statements


class AbortTransaction(Exception):  # Define a custom exception
    '''raise this exception to abort the transaction'''
    pass


def valid_amount(amount):  # amount checked against
    try:
        amount = float(amount)
    except ValueError:
        raise AbortTransaction('Amount must be an integer')
    if amount <= 0:
        raise AbortTransaction('Amount must be positive')
    return amount


class Account:

    def __init__(self, name, balance, password):
        self.name = name
        self.balance = float(balance)
        self.password = password

    def check_password(self, password):
        if password != self.password:
            raise AbortTransaction('Incorrect password for this account')

    def get_deposit(self, amount_to_deposit):
        amount_to_deposit = valid_amount(amount_to_deposit)
        self.balance += amount_to_deposit
        return self.balance

    def get_withdraw(self, amount_to_withdraw):
        amount_to_withdraw = valid_amount(amount_to_withdraw)
        if amount_to_withdraw > self.balance:
            raise AbortTransaction('You cannot withdraw more than you have in your account')
        self.balance -= amount_to_withdraw
        return self.balance

    def get_balance(self):
        return self.balance

    def get_info(self):
        print('Name\t-> {}\nBalance\t-> ₹{:.2f}/-\nPasskey\t-> {}'.format(self.name, self.balance, self.password))


if __name__ == '__main__':
    person = Account('bishwa', 789.43, 'joker')
    person.get_info()
    print(person.get_balance())
