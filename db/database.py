import psycopg2
from dotenv import load_dotenv
from config import DATABASE_CONFIG

# Load environment variables from .env file (only for local development)
load_dotenv()

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=DATABASE_CONFIG["dbname"],
            user=DATABASE_CONFIG["user"],
            password=DATABASE_CONFIG["password"],
            host=DATABASE_CONFIG["host"],
            port=DATABASE_CONFIG["port"],
        )
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()



