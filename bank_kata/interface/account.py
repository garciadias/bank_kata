from abc import ABC, abstractmethod


class AccountInterface(ABC):

    @abstractmethod
    def deposit(self, amount: float) -> None:
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass

    @abstractmethod
    def statement(self) -> str:
        pass
