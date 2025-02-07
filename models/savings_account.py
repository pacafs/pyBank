# models/savings_account.py
from models.bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, account_id: int, customer_id: int, balance: float, interest_rate: float):
        super().__init__(account_id, customer_id, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self) -> float:
        return self.balance

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate