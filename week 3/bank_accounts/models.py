from enum import Enum
from typing import List


class AccountType(Enum):
    KZT = 'KZT'
    USD = 'USD'
    RUB = 'RUB'
    EUR = 'EUR'


class Account:
    cash_amount: float
    account_type: AccountType

    # def __init__(self, cash_amount: str, account_type: AccountType):
    #     self.cash_amount = cash_amount
    #     self.account_type = account_type

    def get_cash_amount(self) -> float:
        return self.cash_amount

    def get_account_type(self) -> AccountType:
        return self.account_type

    def set_cash_amount(self, cash_amount: float) -> None:
        self.cash_amount = cash_amount

    def set_account_type(self, account_type: AccountType) -> None:
        self.account_type = account_type

    def add_to_cash_amount(self, cash):
        self.cash_amount += cash

    def subtract_from_cash_amount(self, cash):
        if self.cash_amount < cash:
            print("Not enough cash")
        else:
            self.cash_amount -= cash

    def money_conversation(self, account_type2: AccountType):
        if self.account_type != account_type2:
            if self.account_type.value == 'KZT' and account_type2.value == "USD":
                self.cash_amount %= 470
                self.account_type = AccountType.USD
            elif self.account_type.value == 'KZT' and account_type2.value == "EUR":
                self.cash_amount %= 496
                self.account_type = AccountType.EUR
            elif self.account_type.value == 'KZT' and account_type2.value == "RUB":
                self.cash_amount %= 7.53
                self.account_type = AccountType.RUB
            elif self.account_type.value == 'USD' and account_type2.value == "KZT":
                self.cash_amount *= 496
                self.account_type = AccountType.KZT
            elif self.account_type.value == 'USD' and account_type2.value == "EUR":
                self.cash_amount %= 1.05
                self.account_type = AccountType.EUR
            elif self.account_type.value == 'USD' and account_type2.value == "RUB":
                self.cash_amount *= 62.52
                self.account_type = AccountType.RUB
            elif self.account_type.value == 'RUB' and account_type2.value == "EUR":
                self.cash_amount %= 65.90
                self.account_type = AccountType.EUR
            elif self.account_type.value == 'RUB' and account_type2.value == "KZT":
                self.cash_amount *= 7.53
                self.account_type = AccountType.KZT
            elif self.account_type.value == 'RUB' and account_type2.value == "USD":
                self.cash_amount %= 62.52
                self.account_type = AccountType.USD
            elif self.account_type.value == 'RUB' and account_type2.value == "EUR":
                self.cash_amount %= 65.90
                self.account_type = AccountType.EUR
            elif self.account_type.value == 'EUR' and account_type2.value == "RUB":
                self.cash_amount *= 65.90
                self.account_type = AccountType.RUB
            elif self.account_type.value == 'EUR' and account_type2.value == "USD":
                self.cash_amount *= 1.05
                self.account_type = AccountType.USD
            elif self.account_type.value == 'EUR' and account_type2.value == "KZT":
                self.cash_amount *= 496
                self.account_type = AccountType.KZT

    def __repr__(self):
        return f'{self.cash_amount} {self.account_type.value}'


class User:
    name: str
    surname: str
    accounts: List[Account]

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.accounts = []

    def __del__(self, account_type: AccountType):
        j = 0
        for i in range(len(self.accounts)):
            if self.accounts[i].account_type.value == account_type.value:
                j = i

        del self.accounts[j]

    def create_account(self, cash_amount: float, account_type: str):
        account = Account()
        if account_type == 'KZT':
            account.set_account_type(account_type=AccountType.KZT)
            account.set_cash_amount(cash_amount=cash_amount)
            self.accounts.append(account)
        elif account_type == 'USD':
            account.set_account_type(account_type=AccountType.USD)
            account.set_cash_amount(cash_amount=cash_amount)
            self.accounts.append(account)
        elif account_type == 'EUR':
            account.set_account_type(account_type=AccountType.EUR)
            account.set_cash_amount(cash_amount=cash_amount)
            self.accounts.append(account)
        elif account_type == 'RUB':
            account.set_account_type(account_type=AccountType.RUB)
            account.set_cash_amount(cash_amount=cash_amount)
            self.accounts.append(account)

    def __repr__(self) -> str:
        return f'{self.name} {self.surname} \n Accounts: \n {self.accounts}'
