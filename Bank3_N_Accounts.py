# Non- OOP Bank
# Version 3
# Any Number of account - With Lists

accountList = []


def show(account_number, Password):
    global accountList
    account = account_number - 1
    if Password != accountList[account]['Password']:
        print("Invalid password!")
    else:
        print('Account\t==> {}\nName\t==> {}\nBalance\t==> {:.2f}\nPasskey\t==> {}'.format(account_number,
                                                                                         accountList[account]['Name'],
                                                                                         accountList[account]['Balance'],
                                                                                         accountList[account]['Password']))


def new_account(name, amount, password):
    global accountList
    new_account_dict = {'Name': name, 'Balance': amount, 'Password': password}
    accountList.append(new_account_dict)
    account_number = len(accountList)
    show(account_number, password)


def get_balance(account_number, Password):
    global accountList
    account = account_number - 1
    if Password != accountList[account]['Password']:
        print("Invalid password!")
        return None
    else:
        return accountList[account]['Balance']


def deposit(account_number, user_deposit_amount, Password):
    global accountList
    account = account_number - 1
    amount = accountList[account]['Balance']
    if 0 < user_deposit_amount:
        if Password != accountList[account]['Password']:
            print('\nInvalid password')
            return None
        else:
            amount += user_deposit_amount
            accountList[account].update({'Balance': amount})
            return amount
    else:
        print('\nInvalid Arguments')
        return None


def withdraw(account_number, user_withdraw_amount, Password):
    global accountList
    account = account_number - 1
    amount = accountList[account]['Balance']
    if 0 < user_withdraw_amount <= amount:
        if Password != accountList[account]['Password']:
            print('\nInvalid password')
            return None
        else:
            amount -= user_withdraw_amount
            accountList[account].update({'Balance': amount})
            return amount
    elif user_withdraw_amount > amount:
        print("\nYou can't withdraw more than you have in your account")
        return None
    else:
        print('\nInvalid Arguments')
        return None


print('\nSample Account!')
new_account('bishwa', 100, 'joker')

while True:
    print('-' * 40)
    print('Welcome to the bank of Maharashtra'.center(40))
    print()
    print('press n to create a new account')
    print('press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account info.')
    print('Press q to quit')
    print()
    action = input('What do you want to do?\n')
    action = action.lower()  # force lower case
    action = action[0]  # Just use first letter
    print()

    if action == 'b':
        try:
            print('{:-^40s}'.format('Balance'))
            userAccount = int(input("Please enter your account number\n"))
            userPassword = input("Please enter your account password\n")
            balance = get_balance(userAccount, userPassword)
            print("Your account balance is: {:.2f}".format(balance))
        except:
            print('\nAn exception occurred, Please Try again!')

    elif action == 'n':
        try:
            print('{:-^40s}'.format('New Account'))
            userName = input('Please enter your name\n')
            userBalance = float(input('Please enter starting amount:'))
            userPassword = input('Please make a passkey\n')
            print('\nYou have successfully created a new account')
            print('{:-^40s}'.format('Account info'))
            new_account(userName, userBalance, userPassword)
        except:
            print('\nAn exception occurred, Please Try again!')

    elif action == 'd':
        try:
            print('{:-^40s}'.format('Deposit'))
            userAccount = int(input("Please enter your account number\n"))
            userDepositAmount = float(input('Please enter amount to deposit:'))
            userPassword = input("Please enter your account password\n")
            D = deposit(userAccount, userDepositAmount, userPassword)
            print("Your account balance is: {:.2f}".format(D))
        except:
            print('\nAn exception occurred, Please Try again!')

    elif action == 'w':
        try:
            print('{:-^40s}'.format('Withdraw'))
            userAccount = int(input("Please enter your account number\n"))
            userWithdrawAmount = float(input('Please enter amount to Withdraw:'))
            userPassword = input("Please enter your account password\n")
            W = withdraw(userAccount, userWithdrawAmount, userPassword)
            print('your new balance is {:.2f}'.format(W))
        except:
            print('\nAn exception occurred, Please Try again!')

    elif action == 's':
        try:
            print('{:-^40s}'.format('Information'))
            userAccount = int(input("Please enter your account number\n"))
            userPassword = input("Please enter your account password\n")
            print('{:-^40s}'.format('Account info'))
            show(userAccount, userPassword)
        except:
            print('\nAn exception occurred, Please Try again!')

    elif action == 'q':
        print('Thank you for using our service.')
        break

    else:
        print('-' * 40)
        print('Invalid Action')
