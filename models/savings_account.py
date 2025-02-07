# models/savings_account.py
from models.bank_account import BankAccount
from db.queries import update_account_balance
class SavingsAccount(BankAccount):
    def __init__(self, account_id: int, customer_id: int, balance: float, interest_rate: float):
        super().__init__(account_id, customer_id, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        update_account_balance(self.account_id, self.balance)

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance >= amount:
            self.balance -= amount
            update_account_balance(self.account_id, self.balance)
        else:
            raise Exception("Insufficient funds")

    def get_balance(self) -> float:
        return self.balance

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
        update_account_balance(self.account_id, self.balance)
