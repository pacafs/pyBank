import os
import psycopg2
from dotenv import load_dotenv
from config import DATABASE_CONFIG

# Load environment variables from .env file (for local development)
load_dotenv()

class Database:
    def __init__(self):
        heroku_db_url = os.getenv("DATABASE_URL")
        if heroku_db_url:
            # Connect using the Heroku-provided DATABASE_URL. Enforce SSL.
            self.conn = psycopg2.connect(heroku_db_url, sslmode='require')
        else:
            # Default to a local configuration defined in config.py/.env.
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

