bank_account = "0 KZT"


def add_to_bank_account(money: float) -> str:
    global bank_account
    bank_account, currency = bank_account.split()
    bank_account = float(bank_account)
    bank_account += money
    bank_account = str(bank_account) + " " + currency
    return bank_account


def subtract_from_bank_account(money: float) -> str:
    global bank_account
    bank_account, currency = bank_account.split()
    bank_account = float(bank_account)
    bank_account -= money
    bank_account = str(bank_account) + " " + currency
    return bank_account


def money_conversion(rate: float, currency1: str, currency2: str) -> str:
    global bank_account
    currency1 = currency1.casefold()
    currency2 = currency2.casefold()
    if currency1 == currency2:
        return bank_account

    bank_account, currency = bank_account.split()
    bank_account = float(bank_account)
    if currency2 == "usd" and currency1 == "kzt":
        bank_account /= rate
        bank_account = str(bank_account) + " USD"
        return bank_account

    bank_account *= rate
    bank_account = str(bank_account) + " KZT"
    return bank_account


print(add_to_bank_account(10000))
print(subtract_from_bank_account(2000))
print(money_conversion(500, "usd", "KZt"))
