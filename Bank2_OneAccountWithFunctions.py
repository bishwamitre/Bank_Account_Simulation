# Non-OOP
# Bank Version 2
# Single Account

accountName = ''
accountBalance = 10000
accountPassword = 'soup'


def new_account(name, balance, Password):
    print('{:-^40s}'.format('New Account'))
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = Password


def info(Password):
    global accountName, accountBalance, accountPassword
    if Password != accountPassword:
        print("Invalid password!")
    else:
        print('\nName\t ==> {}\nBalance  ==> {:.2f}\nPassword ==> {}'.format(accountName, accountBalance,
                                                                             accountPassword))
        print('-' * 40)


def get_balance(Password):
    global accountName, accountBalance, accountPassword
    if Password != accountPassword:
        print("Invalid password!")
    else:
        print("Your account balance is: {:.2f}".format(accountBalance))
        print('-' * 40)


def deposit(user_deposit_amount, Password):
    global accountName, accountBalance, accountPassword
    if user_deposit_amount > 0:
        if Password != accountPassword:
            print('Invalid password')
        else:
            accountBalance += user_deposit_amount
            print('Your new account balance is {:.2f}'.format(accountBalance))
            print('-' * 40)
    else:
        print('Invalid Arguments')


def withdraw(user_withdraw_amount, Password):
    global accountName, accountBalance, accountPassword
    if user_withdraw_amount > 0:
        if Password != accountPassword:
            print('Invalid password')
        elif user_withdraw_amount > accountBalance:
            print('_' * 40)
            print("You can't withdraw more than you have in your account")
        else:
            accountBalance -= user_withdraw_amount
            print('your new balance is {:.2f}'.format(accountBalance))
            print('-' * 40)
    else:
        print('Invalid Arguments')


while True:
    print()
    print('Welcome to the bank of Boshada'.center(40))
    print()
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
        print('{:-^40s}'.format('Balance'))
        userPassword = input("Please enter your account password\n")
        get_balance(userPassword)

    elif action == 'd':
        print('{:-^40s}'.format('Deposit'))
        userDepositAmount = int(input('Please enter amount to deposit:'))
        userPassword = input("Please enter your account password\n")
        deposit(userDepositAmount, userPassword)

    elif action == 'w':
        print('{:-^40s}'.format('Withdraw'))
        userWithdrawAmount = int(input('Please enter amount to Withdraw:'))
        userPassword = input("Please enter your account password\n")
        withdraw(userWithdrawAmount, userPassword)

    elif action == 's':
        print('{:-^40s}'.format('Information'))
        userPassword = input("Please enter your account password\n")
        info(userPassword)

    elif action == 'q':
        break

    else:
        print('_' * 40)
        print('\nInvalid Action')
