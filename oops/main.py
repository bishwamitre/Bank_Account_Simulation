from Bank import *

oBank = Bank()

# sample account
bishwaAccountNumber = oBank.create_account('bishwa', 9.9, 'joker')
print(f'bishwa Account Number:{bishwaAccountNumber}')

while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To open a new account, press o')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w ')
    print()
    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]  # grab the first letter print()
    if action == 'b':
        oBank.balance()
    elif action == 'c':
        oBank.close_account()
    elif action == 'd':
        oBank.amount_deposit()
    elif action == 'o':
        oBank.open_account()
    elif action == 's':
        oBank.info_account()
    elif action == 'q':
        break
    elif action == 'w':
        oBank.amount_withdraw()
    else:
        print('Sorry, that was not a valid action. Please try again.')

print('Done')
