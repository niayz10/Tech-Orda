from typing import Optional

from bank_accounts.models import User
from bank_accounts.repositories import BankAccountRepositories


class BankAccountServices:
    repositories: BankAccountRepositories

    def __init__(self, repositories: BankAccountRepositories):
        self.repositories = repositories

    def create_bank_account(self, name: str, surname: str, cash_amount: float, account_type: str) -> None:
        self.repositories.create_bank_account(name=name, surname=surname,
                                              cash_amount=cash_amount, account_type=account_type)

    def destroy_account(self, name: str, surname: str, account_type: str) -> None:
        self.repositories.destroy_account(name=name, surname=surname, account_type=account_type)

    def get_bank_account(self, name: str, surname: str) -> Optional[User]:
        return self.repositories.get_bank_account(name=name, surname=surname)

    def add_to_bank_account(self, name: str, surname: str, cash: float, account_type: str) -> None:
        self.repositories.add_to_bank_account(name=name, surname=surname, cash=cash, account_type=account_type)

    def subtract_from_bank_account(self, name: str, surname: str, cash: float, account_type: str) -> None:
        self.repositories.subtract_from_bank_account(name=name, surname=surname, cash=cash, account_type=account_type)

    def money_conversation(self, name: str, surname: str, account_type1: str, account_type2: str) -> None:
        self.repositories.money_conversation(name=name, surname=surname,
                                             account_type1=account_type1, account_type2=account_type2)
