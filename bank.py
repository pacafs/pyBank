# bank.py
from models.customer import Customer
from models.checking_account import CheckingAccount
from models.savings_account import SavingsAccount
from db.queries import create_customer, create_account, make_transaction, apply_interest

class Bank:
    def __init__(self):
        pass

    def create_customer(self, name: str, email: str, password: str) -> Customer:
        customer_id = create_customer(name, email, password)
        return Customer(customer_id, name, email, password)

    def create_account(self, customer_id: int, acc_type: str, initial_balance: float):
        account_id = create_account(customer_id, acc_type, initial_balance)
        if acc_type == "checking":
            return CheckingAccount(account_id, customer_id, initial_balance, overdraft_limit=1000)
        elif acc_type == "savings":
            return SavingsAccount(account_id, customer_id, initial_balance, interest_rate=0.03)

    def process_transaction(self, sender_id: int, receiver_id: int, amount: float):
        make_transaction(sender_id, receiver_id, amount)
        print("Transaction processed.")

    def apply_interest(self):
        apply_interest()

