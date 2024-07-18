from bank_kata.interface.account import AccountInterface


class Account: ...


class AccountService(AccountInterface):

    def deposit(self, amount: float, acount: Account) -> None:
        return None

    def withdraw(self, amount: float, acount: Account) -> None:
        return None

    def statement(self, account: Account) -> str:
        return ""
