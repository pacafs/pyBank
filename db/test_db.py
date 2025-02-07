# test_db_connection.py
from database import Database
from config import DATABASE_CONFIG

try:
    db = Database()
    print(f"✅ Connected to PostgreSQL database: {DATABASE_CONFIG['dbname']}")
    db.close()
except Exception as e:
    print(f"❌ Connection failed: {e}")