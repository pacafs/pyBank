# test_db_connection.py
from db.database import Database
from db.config import DATABASE_CONFIG

try:
    db = Database()
    print(f"✅ Connected to PostgreSQL database: {DATABASE_CONFIG['dbname']}")

    # Fetch PostgreSQL version
    result = db.fetchone("SELECT version();")
    print(f"PostgreSQL Version: {result[0]}")

    db.close()
except Exception as e:
    print(f"❌ Connection failed: {e}")
