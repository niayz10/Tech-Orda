from typing import Optional

from bank_accounts.models import User
from bank_accounts.services import BankAccountServices


class BankAccountHandlers:
    bank_account_services: BankAccountServices

    def __init__(self, services: BankAccountServices):
        self.bank_account_services = services

    def open_bank_account(self, name: str, surname: str, cash_amount: float, account_type: str) -> None:
        name = name.strip()
        surname = surname.strip()
        account_type = account_type.strip().upper()

        self.bank_account_services.create_bank_account(name=name, surname=surname,
                                                       cash_amount=cash_amount, account_type=account_type)

    def delete_account(self, name: str, surname: str, account_type: str) -> None:
        name = name.strip()
        surname = surname.strip()
        account_type = account_type.strip().upper()
        self.bank_account_services.destroy_account(name=name, surname=surname, account_type=account_type)

    def view_bank_account(self, name: str, surname: str) -> Optional[User]:
        name = name.strip()
        surname = surname.strip()

        return self.bank_account_services.get_bank_account(name=name, surname=surname)

    def add_cash(self, name: str, surname: str, cash: float, account_type: str) -> None:
        name = name.strip()
        surname = surname.strip()
        account_type = account_type.strip().upper()
        cash = float(cash)
        if cash > 0:
            self.bank_account_services.add_to_bank_account(name=name, surname=surname,
                                                           cash=cash, account_type=account_type)

    def subtract_cash(self, name: str, surname: str, cash: float, account_type: str) -> None:
        name = name.strip()
        surname = surname.strip()
        account_type = account_type.strip().upper()
        cash = float(cash)
        if cash > 0:
            self.bank_account_services.subtract_from_bank_account(name=name, surname=surname,
                                                                  cash=cash, account_type=account_type)

    def money_conversation(self, name: str, surname: str, account_type1: str, account_type2: str) -> None:
        name = name.strip()
        surname = surname.strip()
        account_type1 = account_type1.strip().upper()
        account_type2 = account_type2.strip().upper()

        self.bank_account_services.money_conversation(name=name, surname=surname,
                                                      account_type1=account_type1, account_type2=account_type2)
