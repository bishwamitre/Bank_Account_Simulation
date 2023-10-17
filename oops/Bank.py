from Account import *


class Bank:
    def __init__(self):
        self.accountsDict = {}
        self.nextAccountNumber = 1023

    def create_account(self, Name, Amount, Password):
        o_account = Account(Name, Amount, Password)
        account_number = self.nextAccountNumber
        self.accountsDict[account_number] = o_account
        self.nextAccountNumber += 1
        return account_number

    def open_account(self):
        userName = input("Please Enter Your Name\n")
        userStartAmount = float(input("Please Enter The Starting Balance:"))
        userPassword = input("Please Enter Password For This Account:\n")
        NewAccount = self.create_account(userName, userStartAmount, userPassword)
        print(f'Your Account Number is: {NewAccount}')

    def close_account(self):
        userAccount = int(input("Please Enter Your Account Number:"))
        userPassword = input("Please Enter Your Account Password:\n")
        o_account = self.accountsDict[userAccount]
        balance = o_account.getbalance(userPassword)
        if balance is not None:
            print(f'You had {balance} in your account which is being return to you')
            self.accountsDict.pop(userAccount)
        else:
            self.accountsDict.pop(userAccount)
            print('You account now closed.')

    def amount_deposit(self):
        userAccount = int(input("Please Enter Your Account Number:"))
        deposit_amount = float(input('Please Enter Amount To Deposit:'))
        userPassword = input("Please Enter Your Account Password:\n")
        o_Account = self.accountsDict[userAccount]
        balance = o_Account.deposit(deposit_amount, userPassword)
        print(f'Now your current account balance is:{balance}')

    def amount_withdraw(self):
        userAccount = int(input("Please Enter Your Account Number:"))
        withdraw_amount = float(input('Please Enter Amount To Deposit:'))
        userPassword = input("Please Enter Your Account Password:\n")
        o_Account = self.accountsDict[userAccount]
        balance = o_Account.withdraw(withdraw_amount, userPassword)
        print(f'Your new balance is:{balance}')

    def info_account(self):
        userAccount = int(input("Please Enter Your Account Number:"))
        userPassword = input("Please Enter Your Account Password:\n")
        o_Account = self.accountsDict[userAccount]
        o_Account.show(userPassword)

    def balance(self):
        userAccount = int(input("Please Enter Your Account Number:"))
        userPassword = input("Please Enter Your Account Password:\n")
        o_Account = self.accountsDict[userAccount]
        o_Account.getbalance(userPassword)


if __name__ == '__main__':
    oBank = Bank()
    oBank.create_account('bishwa', 89, 'joker')
    oBank.create_account('mama', 1000, 'joker')
    oBank.close_account()
    print(oBank.accountsDict)
