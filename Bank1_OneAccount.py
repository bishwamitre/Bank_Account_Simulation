#Non-OOP
#Bank Version 1
#Single Account

accountName = 'Bishwa Mitre'
accountBalance = 1000
accountPassword = 'soup'

while True:
    print('_'*40)
    print()
    print('Welcome to the bank of Boshda'.center(40))
    print()
    print('press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawal')
    print('Press s to show the account info.')
    print('Press q to quit')
    print('_'*40)
    print()
    action = input('What do you want to do?\n')
    action = action.lower()     # force lower case
    action = action[0]          # Just use first letter
    print()

    if action == 'b':
        print('{:-^40s}'.format('Balance'))
        userPassword = input("Please enter your account password\n")
        if userPassword != accountPassword:
            print('_'*40)
            print("\nInvalid password!")
        else:
            print('_'*40)
            print("\nYour account balance is:{:.2f}".format(accountBalance) )

    elif action == 'd':
        print('{:-^40s}'.format('Deposit'))
        userDepositAmount = input('Please enter amount to deposit:')
 
        if userDepositAmount.isdigit() and int(userDepositAmount) > 0 :
            userPassword = input("Please enter your account password\n")
            if userPassword != accountPassword:
                print('_'*40)
                print('\nInvalid password')
            else:
                accountBalance += int(userDepositAmount)
                print('_'*40)
                print('\nYour new account balance is {}'.format(accountBalance))
        else:
            print('_'*40)
            print('\nInvalid Arguments')
        

    elif action == 's':
        print('{:-^40s}'.format('Information'))
        userPassword = input("Please enter your account password\n")
        if userPassword != accountPassword:
                print('_'*40)
                print('\nInvalid password')
        else:
            print('_'*40)
            print('\nName\t ==> {}\nBalance  ==> {:.2f}\nPassword ==> {}'.format(accountName,accountBalance,accountPassword))

    elif action == 'w':
        print('{:-^40s}'.format('Withdraw'))
        userWithdrawAmount = input('Please enter amount to Withdraw:')
        if userWithdrawAmount.isdigit() and int(userWithdrawAmount) > 0 :
                userWithdrawAmount = int(userWithdrawAmount)
                userPassword = input("Please enter your account password\n")
                if userPassword != accountPassword:
                    print('_'*40)
                    print('\nInvalid password')
                elif userWithdrawAmount > accountBalance:
                    print("You can't withdraw more than you have in your account")
                else:
                    accountBalance -= userWithdrawAmount
                    print('_'*40)
                    print('\nyour new balance is {:.2f}'.format(accountBalance))
        else:
            print('_'*40)
            print('\nInvalid Arguments')

    elif action == 'q':
        break
    
    else:
        print('_'*40)
        print('\nInvalid Action')
 
