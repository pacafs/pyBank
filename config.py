import os
from dotenv import load_dotenv

load_dotenv()

# Default to local database, but override if deployed (Render)
DATABASE_CONFIG = {
    "dbname": os.environ["DB_NAME"],  # Default: local DB
    "user": os.environ["DB_USER"],
    "password": os.environ["DB_PASSWORD"],
    "host": os.environ["DB_HOST"],
    "port": os.environ["DB_PORT"],
}

