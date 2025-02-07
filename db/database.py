# database.py
import psycopg2
from psycopg2 import sql
from config import DATABASE_CONFIG
from typing import List

class Database:
    def __init__(self):
        """Initialize database connection."""
        self.conn = psycopg2.connect(**DATABASE_CONFIG)
        self.cursor = self.conn.cursor()
        self._create_tables()

    def _create_tables(self):
        """Create necessary tables if they don't exist."""
        queries = [
            """
            CREATE TABLE IF NOT EXISTS customers (
                customer_id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS accounts (
                account_id SERIAL PRIMARY KEY,
                customer_id INTEGER NOT NULL,
                type TEXT NOT NULL CHECK (type IN ('checking', 'savings')),
                balance NUMERIC(15,2) NOT NULL DEFAULT 0.00,
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS transactions (
                transaction_id SERIAL PRIMARY KEY,
                sender_id INTEGER NOT NULL,
                receiver_id INTEGER NOT NULL,
                amount NUMERIC(15,2) NOT NULL CHECK (amount > 0),
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (sender_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
                FOREIGN KEY (receiver_id) REFERENCES customers(customer_id) ON DELETE CASCADE
            );
            """
        ]
        
        for query in queries:
            self.cursor.execute(query)
        
        self.conn.commit()

    def execute(self, query: str, params: tuple = ()):
        """Execute a write operation (INSERT, UPDATE, DELETE)."""
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetchall(self, query: str, params: tuple = ()) -> List[tuple]:
        """Execute a read operation and return all results."""
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetchone(self, query: str, params: tuple = ()) -> tuple:
        """Execute a read operation and return a single result."""
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def close(self):
        """Close the database connection."""
        self.cursor.close()
        self.conn.close()
