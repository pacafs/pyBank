from db.database import Database

def migrate():
    db = Database()
    
    # List of migration queries to create tables with relationships.
    migrations = [
        '''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        );
        ''',
        '''
        CREATE TABLE IF NOT EXISTS accounts (
            account_id SERIAL PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            type VARCHAR(20) NOT NULL,
            balance NUMERIC(12,2) NOT NULL DEFAULT 0,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
        );
        ''',
        '''
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id SERIAL PRIMARY KEY,
            sender_id INTEGER NOT NULL,
            receiver_id INTEGER NOT NULL,
            amount NUMERIC(12,2) NOT NULL,
            timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (sender_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
            FOREIGN KEY (receiver_id) REFERENCES customers(customer_id) ON DELETE CASCADE
        );
        '''
    ]

    try:
        for query in migrations:
            db.cursor.execute(query)
        db.conn.commit()
        print("Migration successful: tables created.")
    except Exception as e:
        db.conn.rollback()
        print("Migration failed:", e)
    finally:
        db.close()

if __name__ == "__main__":
    migrate()
