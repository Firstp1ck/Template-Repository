import os
import logging
from dotenv import load_dotenv
from typing import Optional

# Setup logging
logging.basicConfig(level=logging.INFO)

def load_environment_variables() -> None:
    """Load environment variables from the .env file."""
    try:
        load_dotenv()  # This function will look for an .env file and load variables from it
        logging.info("Environment variables loaded successfully.")
    except Exception as e:
        logging.error(f"Failed to load environment variables: {e}")

def get_env_variable(key: str) -> Optional[str]:
    """Get an environment variable by key with error handling."""
    try:
        value = os.getenv(key)
        if value is None:
            logging.warning(f"{key} is not set in the environment variables.")
        return value
    except Exception as e:
        logging.error(f"Error accessing {key}: {e}")
        return None

# Main execution
if __name__ == "__main__":
    load_environment_variables()
    api_key = get_env_variable('API_KEY')
    database_url = get_env_variable('DATABASE_URL')
    secret_key = get_env_variable('SECRET_KEY')

    if api_key and database_url and secret_key:
        print(f"API Key: {api_key}")
        print(f"Database URL: {database_url}")
        print(f"Secret Key: {secret_key}")
    else:
        logging.error("One or more environment variables are missing.")