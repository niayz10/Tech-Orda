import sys

from bank_accounts.handlers import BankAccountHandlers
from bank_accounts.repositories import BankAccountRepositories
from bank_accounts.services import BankAccountServices


def init():
    bank_account_repositories = BankAccountRepositories()
    bank_account_services = BankAccountServices(repositories=bank_account_repositories)
    bank_account_handlers = BankAccountHandlers(services=bank_account_services)

    while True:
        print("Commands: \n 1. Open bank account \n 2. View bank account "
              "\n 3. Add to bank account \n 4. Subtract from bank Account \n 5. Convert money \n 6. Delete account")
        command = input("Enter command or q (quit) to exit: ")

        if command == 'q':
            sys.exit(0)

        if command == '1':
            name, surname = input('Please enter name and surname: ').split()
            cash_amount, account_type = input('Enter your cash and currency: ').split()
            bank_account_handlers.open_bank_account(name=name, surname=surname,
                                                    cash_amount=float(cash_amount), account_type=account_type)

        elif command == '2':
            name, surname = input('Please enter your name and surname: ').split()
            print(bank_account_handlers.view_bank_account(name=name, surname=surname))

        elif command == '3':
            name, surname = input('Please enter your name and surname: ').split()
            cash, account_type = input('Enter your cash and currency: ').split()
            bank_account_handlers.add_cash(name=name, surname=surname, cash=cash, account_type=account_type)

        elif command == '4':
            name, surname = input('Please enter your name and surname: ').split()
            cash, account_type = input('Enter your cash and currency: ').split()
            bank_account_handlers.subtract_cash(name=name, surname=surname, cash=cash, account_type=account_type)

        elif command == '5':
            name, surname = input('Please enter your name and surname: ').split()
            account_type1, account_type2 = input('Enter the currency of your account and the currency you want to '
                                                 'exchange: ').split()
            bank_account_handlers.money_conversation(name=name, surname=surname,
                                                     account_type1=account_type1, account_type2=account_type2)
        elif command == '6':
            name, surname = input('Please enter your name and surname: ').split()
            account_type = input("Enter currency: ")
            bank_account_handlers.delete_account(name=name, surname=surname, account_type=account_type)

        else:
            print(f'invalid command {command}')


if __name__ == '__main__':
    init()
