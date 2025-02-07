# config.py
import os

# Default to local database, but override if deployed (Render)
DATABASE_CONFIG = {
    "dbname": os.getenv("DB_NAME", "flaskBank"),  # Default: local DB
    "user": os.getenv("DB_USER", "paca"),
    "password": os.getenv("DB_PASSWORD", "barcelos1"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
}
