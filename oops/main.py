from Bank import *

oBank = Bank('9 to 5', 'B block, Shah bad dairy, new delhi', "(+91)9899999799")


# sample account
bishwaAccountNumber = oBank.create_account('bishwa', 9.9, 'joker')
print(f'bishwa Account Number:{bishwaAccountNumber}')

while True:
    print()
    print('To get an account balance, press b')
    print('To close an account, press c')
    print('To make a deposit, press d')
    print('To get bank info, press n' )
    print('To open a new account, press o')
    print('To show account info, press i')
    print('To quit, press q')
    print('To show all accounts, press s')
    print('To make a withdrawal, press w ')
    print()

    try:
        action = input('What do you want to do? ')
        action = action.lower()
        action = action[0]  # grab the first letter print()
    except IndexError:
        print('Please choose key')

    try:
        if action == 'b':
            oBank.balance()
        elif action == 'o':
            oBank.open_account()
        elif action == 'c':
            oBank.close_account()
        elif action == 'd':
            oBank.amount_deposit()
        elif action == 'w':
            oBank.amount_withdraw()
        elif action == 'i':
            oBank.info_account()
        elif action == 'n':
            oBank.bank_info()
        elif action == 's':
            oBank.show()
        elif action == 'q':
            break
    except AbortTransaction as error:
        print(error)

print('Done')

