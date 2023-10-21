from Account import *


def valid_password(oAccount):
    account_password = input('What is your account password: ')
    oAccount.check_password(account_password)


class Bank:
    def __init__(self, hours, address, phone):
        self.accountsDict = {}
        self.nextAccountNumber = 1023
        self.Hour = hours
        self.address = address
        self.phone = phone
        self.adminPassword = 'admin@2005'

    def valid_account_number(self):
        account_no = input('What is you account number: ')
        try:
            account_no = int(account_no)
        except ValueError:
            raise AbortTransaction('The account number must be an integer!')
        if account_no not in self.accountsDict:
            raise AbortTransaction('There is no account number ' + str(account_no))
        return account_no

    def get_account_number(self):
        account_no = self.valid_account_number()
        o_account = self.accountsDict[account_no]
        valid_password(o_account)
        return o_account

    def create_account(self, Name, Amount, Password):
        o_account = Account(Name, Amount, Password)
        account_no = self.nextAccountNumber
        self.accountsDict[account_no] = o_account
        self.nextAccountNumber += 1
        return account_no

    def open_account(self):
        print('{:-^40s}'.format('New Account'))
        user_name = input("Please Enter Your Name\n")
        user_start_amount = float(input("Please Enter The Starting Balance:"))
        user_password = input("Please Enter Password For This Account:\n")
        new_account = self.create_account(user_name, user_start_amount, user_password)
        print(f'Your Account Number is: {new_account}')

    def close_account(self):
        print('{:-^40s}'.format('Close Account'))
        account_no = self.valid_account_number()
        o_account = self.accountsDict[account_no]
        balance = o_account.get_balance()
        if balance is not None:
            print(f'You had ₹{balance}/- in your account which is being return to you.')
            self.accountsDict.pop(account_no)
        else:
            self.accountsDict.pop(account_no)
            print('You account now closed.')

    def amount_deposit(self):
        print('{:-^40s}'.format('Deposit'))
        account_no = self.get_account_number()
        amount = input('Please enter amount to deposit: ')
        balance = account_no.get_deposit(amount)
        print(f'deposited:₹{amount}/-')
        print(f'Your new account balance is:₹{balance}/-')

    def amount_withdraw(self):
        print('{:-^40s}'.format('Withdraw'))
        account_no = self.get_account_number()
        amount = input('Please Enter Amount To withdraw:')
        balance = account_no.get_withdraw(amount)
        print(f'Withdrew:₹{amount}/-')
        print(f'Your new account balance is:₹{balance}/-')

    def balance(self):
        print('{:-^40s}'.format('Balance'))
        account_no = self.get_account_number()
        balance = account_no.get_balance()
        print("Your current account balance is: ₹{:.2f}/-".format(balance))

    def info_account(self):
        print('{:-^40s}'.format('Information'))
        account_no = self.get_account_number()
        return account_no.get_info()

    def bank_info(self):
        print('{:-^40s}'.format('Bank Info'))
        print('Hours:', self.Hour)
        print('Address:', self.address)
        print('Phone:', self.phone)
        print('We currently have', len(self.accountsDict), 'account(s) open.')

    def show(self):
        print('{:-^40s}'.format('Admin'))
        print('This would typically require an admin password:')
        password = input()
        if password != self.adminPassword:
            print('This would require an admin password')
        else:
            for userAccountNumber in self.accountsDict:
                o_account = self.accountsDict[userAccountNumber]
                print(f'Account: {o_account}')
                o_account.get_info()
                print()


if __name__ == '__main__':
    oBank = Bank('9 to 5', 'B block, Shah bad dairy, new delhi', "(+91)983424323")
    account_number = oBank.create_account('bishwa', 999.9, 'joker')
    account_number1 = oBank.create_account('Ashok', 334.32, 'Nun')
