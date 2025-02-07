# models/customer.py
from typing import List
from models.checking_account import CheckingAccount
from models.savings_account import SavingsAccount
from db.queries import fetchall

class Customer:
    def __init__(self, customer_id: int, name: str, email: str, password: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.password = password

    def get_accounts(self) -> List:
        accounts_data = fetchall("SELECT * FROM accounts WHERE customer_id=%s", (self.customer_id,))
        accounts = []
        for account_data in accounts_data:
            account_id, customer_id, acc_type, balance = account_data
            if acc_type == "checking":
                accounts.append(CheckingAccount(account_id, customer_id, balance, overdraft_limit=1000))
            elif acc_type == "savings":
                accounts.append(SavingsAccount(account_id, customer_id, balance, interest_rate=0.03))
        return accounts
    
    