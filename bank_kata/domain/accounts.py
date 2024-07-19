from datetime import datetime
from typing import List

from pydantic import BaseModel

from bank_kata.interface.account import AccountInterface

HEADER_STATEMENT = "Date       || Amount || Balance"


class TransactionInfo(BaseModel):
    date: str
    amount: float
    balance: float


class Account:
    balance: float = 0.0
    history: List[TransactionInfo] = []
    statement: str = HEADER_STATEMENT


class AccountService(AccountInterface):

    def deposit(self, acount: Account, amount: float) -> None:
        acount.balance += amount
        today = datetime.today().strftime("%d-%m-%Y")
        acount.history.append(
            TransactionInfo(date=today, amount=amount, balance=acount.balance)
        )
        acount.statement += f"\n{today} || {amount:0.0f}   || {acount.balance:0.0f}"

        return None

    def withdraw(self, acount: Account, amount: float) -> None:
        acount.balance -= amount
        return None

    def statement(self, account: Account) -> str:
        print(account.statement)
        return None
