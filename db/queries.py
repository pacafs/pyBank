import datetime

# Global variable for the database connection.
db = None

def set_db(connection):
    """
    Sets the global database connection.
    
    This should be called early in your application startup (for example, in main.py)
    to initialize the db connection before any queries are executed.
    """
    global db
    db = connection

def execute(query, params=()):
    """
    Executes a query on the global database connection and commits the changes.
    """
    if db is None:
        raise Exception("Database connection not initialized. Please call set_db() first.")
    db.cursor.execute(query, params)
    db.conn.commit()

def fetchone(query, params=()):
    """
    Executes a query and returns a single result from the global database connection.
    """
    if db is None:
        raise Exception("Database connection not initialized. Please call set_db() first.")
    db.cursor.execute(query, params)
    return db.cursor.fetchone()

def fetchall(query, params=()):
    """
    Executes a query and returns all results from the global database connection.
    """
    if db is None:
        raise Exception("Database connection not initialized. Please call set_db() first.")
    db.cursor.execute(query, params)
    return db.cursor.fetchall()

def update_account_balance(account_id, balance):
    """
    Updates the balance for a given account.
    """
    query = "UPDATE accounts SET balance=%s WHERE account_id=%s"
    execute(query, (balance, account_id))

def create_customer(name, email, password):
    """
    Inserts a new customer into the database and returns the customer ID.
    """
    query = (
        "INSERT INTO customers (name, email, password) VALUES (%s, %s, %s) "
        "RETURNING customer_id"
    )
    result = fetchone(query, (name, email, password))
    return result[0]

def create_account(customer_id, acc_type, initial_balance):
    """
    Inserts a new account into the database and returns the account ID.
    """
    query = (
        "INSERT INTO accounts (customer_id, type, balance) VALUES (%s, %s, %s) "
        "RETURNING account_id"
    )
    result = fetchone(query, (customer_id, acc_type, initial_balance))
    return result[0]

def process_transaction(sender_id, receiver_id, amount):
    """
    Inserts a new transaction into the database.
    """
    query = "INSERT INTO transactions (sender_id, receiver_id, amount, timestamp) VALUES (%s, %s, %s, %s)"
    execute(query, (sender_id, receiver_id, amount, datetime.datetime.now()))

def apply_interest():
    """
    Applies interest to all savings accounts by selecting them and updating their balances.
    """
    query = "SELECT * FROM accounts WHERE type='savings'"
    accounts = fetchall(query)
    for account_data in accounts:
        account_id, customer_id, acc_type, balance = account_data
        new_balance = balance + balance * 0.03
        update_query = "UPDATE accounts SET balance=%s WHERE account_id=%s"
        execute(update_query, (new_balance, account_id))
