from abc import ABC, abstractmethod
# Abstract Base Class for BankAccount
class BankAccount(ABC):
    def __init__(self, account_id: int, customer_id: int, balance: float):
        self.account_id = account_id
        self.customer_id = customer_id
        self.balance = balance

    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    @abstractmethod
    def get_balance(self) -> float:
        pass
