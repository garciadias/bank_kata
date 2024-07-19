from abc import ABC, abstractmethod


class AccountInterface(ABC):

    @abstractmethod
    def deposit(self, amount: float) -> None: ...

    @abstractmethod
    def withdraw(self, amount: float) -> None: ...

    @abstractmethod
    def statement(self) -> str: ...
