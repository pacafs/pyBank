# models/transaction.py
from datetime import datetime

class Transaction:
    def __init__(self, transaction_id: int, sender_id: int, receiver_id: int, amount: float, timestamp: datetime):
        self.transaction_id = transaction_id
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.amount = amount
        self.timestamp = timestamp