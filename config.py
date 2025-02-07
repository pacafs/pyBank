import os
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env", override=True)

def get_database_config():
    """
    Returns database configuration.
    
    If a Heroku DATABASE_URL is provided in the environment (i.e., in production),
    parse it and return the corresponding values. Otherwise, fall back to the local
    .env defined variables.
    """
    # Check for Heroku's DATABASE_URL
    database_url = os.environ.get("DATABASE_URL")
    if database_url:
        parsed_url = urlparse(database_url)
        return {
            "dbname": parsed_url.path.lstrip("/"),
            "user": parsed_url.username,
            "password": parsed_url.password,
            "host": parsed_url.hostname,
            "port": parsed_url.port,
        }
    else:
        # Use local variables from .env
        return {
            "dbname": os.getenv("DB_NAME"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "host": os.getenv("DB_HOST"),
            "port": int(os.getenv("DB_PORT", 5432)),  # Fall back to port 5432
        }

DATABASE_CONFIG = get_database_config()