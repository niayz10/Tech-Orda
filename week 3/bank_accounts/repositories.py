from typing import List, Optional

from bank_accounts.models import User, AccountType


class BankAccountRepositories:
    users: List[User] = []

    def create_bank_account(self, name: str, surname: str, cash_amount: float, account_type: str) -> None:
        if next((b for b in self.users if name == b.name and surname == b.surname), None):
            bank_account = self.get_bank_account(name=name, surname=surname)
            bank_account.create_account(cash_amount=cash_amount, account_type=account_type)
        else:
            bank_account = User(name=name, surname=surname)
            bank_account.create_account(cash_amount=cash_amount, account_type=account_type)

        self.users.append(bank_account)

    def destroy_account(self, name: str, surname: str, account_type: str) -> None:

        bank_account = next((b for b in self.users if name == b.name and surname == b.surname), None)
        if bank_account:
            if account_type == "KZT":
                bank_account.__del__(account_type=AccountType.KZT)
            elif account_type == "USD":
                bank_account.__del__(account_type=AccountType.USD)
            elif account_type == "RUB":
                bank_account.__del__(account_type=AccountType.RUB)
            elif account_type == "EUR":
                bank_account.__del__(account_type=AccountType.EUR)

    def get_bank_account(self, name: str, surname: str) -> Optional[User]:
        bank_account = next((b for b in self.users if name == b.name and surname == b.surname), None)

        if not bank_account:
            print("Bank account not found")
            return

        return bank_account

    def add_to_bank_account(self, name: str, surname: str, cash: float, account_type: str) -> None:
        bank_account = next((b for b in self.users if name == b.name and surname == b.surname), None)

        for a in bank_account.accounts:
            if a.account_type.value == account_type:
                a.add_to_cash_amount(cash=cash)
                break

    def subtract_from_bank_account(self, name: str, surname: str, cash: float, account_type: str) -> None:
        bank_account = next((b for b in self.users if name == b.name and surname == b.surname), None)

        for a in bank_account.accounts:
            if a.account_type.value == account_type:
                a.subtract_from_cash_amount(cash=cash)
                break

    def money_conversation(self, name: str, surname: str, account_type1: str, account_type2: str) -> None:
        bank_account = next((b for b in self.users if name == b.name and surname == b.surname), None)
        for a in bank_account.accounts:
            if a.account_type.value == account_type1:
                if account_type2 == "RUB":
                    a.money_conversation(account_type2=AccountType.RUB)
                    break
                if account_type2 == "EUR":
                    a.money_conversation(account_type2=AccountType.EUR)
                    break
                if account_type2 == "KZT":
                    a.money_conversation(account_type2=AccountType.KZT)
                    break
                if account_type2 == "USD":
                    a.money_conversation(account_type2=AccountType.USD)
                    break
