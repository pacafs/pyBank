# models/checking_account.py
from models.bank_account import BankAccount
from db.queries import update_account_balance

class CheckingAccount(BankAccount):
    def __init__(self, account_id: int, customer_id: int, balance: float, overdraft_limit: float):
        super().__init__(account_id, customer_id, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            update_account_balance(self.account_id, self.balance)
        else:
            print("Insufficient funds")

    def get_balance(self) -> float:
        return self.balance