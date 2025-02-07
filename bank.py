# bank.py
from models.customer import Customer
from models.checking_account import CheckingAccount
from models.savings_account import SavingsAccount
from db.database import Database
from datetime import datetime

class Bank:
    def __init__(self, db: Database):
        self.db = db

    def create_customer(self, name: str, email: str, password: str) -> Customer:
        # Using RETURNING clause to fetch the auto-generated customer_id
        insert_query = (
            "INSERT INTO customers (name, email, password) VALUES (%s, %s, %s) "
            "RETURNING customer_id"
        )
        self.db.cursor.execute(insert_query, (name, email, password))
        customer_id = self.db.cursor.fetchone()[0]
        self.db.conn.commit()
        return Customer(customer_id, name, email, password)

    def create_account(self, customer_id: int, acc_type: str, initial_balance: float):
        # Using RETURNING clause to fetch the auto-generated account_id
        insert_query = (
            "INSERT INTO accounts (customer_id, type, balance) VALUES (%s, %s, %s) "
            "RETURNING account_id"
        )
        self.db.cursor.execute(insert_query, (customer_id, acc_type, initial_balance))
        account_id = self.db.cursor.fetchone()[0]
        self.db.conn.commit()

        if acc_type == "checking":
            return CheckingAccount(account_id, customer_id, initial_balance, overdraft_limit=1000)
        elif acc_type == "savings":
            return SavingsAccount(account_id, customer_id, initial_balance, interest_rate=0.03)

    def process_transaction(self, sender_id: int, receiver_id: int, amount: float):
        self.db.execute(
            "INSERT INTO transactions (sender_id, receiver_id, amount, timestamp) VALUES (%s, %s, %s, %s)",
            (sender_id, receiver_id, amount, datetime.now()),
        )
        print("Transaction processed.")

    def apply_interest(self):
        accounts = self.db.fetchall("SELECT * FROM accounts WHERE type='savings'")
        for account_data in accounts:
            account_id, customer_id, acc_type, balance = account_data
            account = SavingsAccount(account_id, customer_id, balance, interest_rate=0.03)
            account.apply_interest()
            self.db.execute("UPDATE accounts SET balance=%s WHERE account_id=%s", (account.get_balance(), account_id))