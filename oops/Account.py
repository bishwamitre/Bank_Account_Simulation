class Account:

    def __init__(self, name, balance, password):
        self.name = name
        self.balance = float(balance)
        self.password = password
    
    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        elif amountToDeposit < 0:
            print('You cannot deposit a negative amount') 
            return None
        else:
            self.balance += amountToDeposit
            return self.balance
        
    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        elif amountToWithdraw < 0:
            print('You cannot withdraw a negative amount')
            return None
        elif amountToWithdraw > self.balance:
            print('You cannot withdraw more than you have in your account')
            return None
        self.balance -= amountToWithdraw
        return self.balance
    
    def getbalance(self, password):
        if password != self.password: 
            print('Sorry, incorrect password') 
            return None
        else:
            return self.balance

    def show(self, password):
        if password != self.password: 
            print('Sorry, incorrect password') 
            return None
        else:
            print('Name\t==> {}\nBalance\t==> {:.2f}\nPasskey\t==> {}'.format(self.name, self.balance, self.password))


if __name__ == '__main__':
    person = Account('bishwa', 100, 'joker')
    person.show('joker')
    person.deposit(199.456, 'joker')
    print('\nAfter deposit\n')
    person.show('joker')
