import logging
import os
from dotenv import load_dotenv
from typing import Optional, List, Dict
import configparser
import sqlite3




# LOGGING HANDLER
def setup_logging(logfile_path='app.log'):
    # Remove all existing handlers
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    
    # Now set up logging with a timestamp
    logging.basicConfig(
        filename=logfile_path,
        filemode='w',
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'  # This sets the date-time format
    )
    logging.debug("Logging initialized successfully")




# CONFIG HANDLER
def validate_file_path(file_path: str) -> bool:
    """ Validate if the provided file_path exists and is accessible """
    try:
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        logging.info(f"File path '{file_path}' validated.")
        return True
    except Exception as e:
        logging.error(e)
        return False
    
def validate_and_print_paths(config: configparser.ConfigParser, section: str, keys: List[str]) -> None:
    """ General function to validate and log file paths based on config """
    try:
        # Loop through all the provided keys in the section
        for key in keys:
            path = config[section][key]
            if validate_file_path(path):
                print(path)
            else:
                logging.warning(f"Invalid path: {path}")
    except KeyError as e:
        logging.error(f"KeyError while accessing config: {e}")
        raise e




# ENV Handler
def load_environment_variables() -> None:
    """Load environment variables from the .env file."""
    try:
        load_dotenv()  # This function will look for an .env file and load variables from it
        logging.info("Environment variables loaded successfully.")
    except Exception as e:
        logging.error(f"Failed to load environment variables: {e}")

def get_env_variable(key: str) -> str:
    """ Fetches the environment variable value associated with key. """
    try:
        value = os.getenv(key)
        if value is None:
            raise ValueError(f"Environment variable '{key}' not found.")
        logging.info(f"Successfully fetched environment variable: {key}")
        return value
    except ValueError as ve:
        logging.error(ve)
        return ""
    except Exception as e:
        logging.error(f"Unexpected error fetching {key}: {e}")
        return ""

def get_multiple_env_variables(var_keys: List[str]) -> Dict[str, str]:
    """
    Fetch multiple environment variables, returns a dictionary with key-value pairs.
    """
    env_variables = {}
    for key in var_keys:
        env_value = get_env_variable(key)
        if env_value == "":
            logging.warning(f"Environment variable '{key}' is missing or empty.")
        else:
            env_variables[key] = env_value
    return env_variables

def mask_sensitive_value(value: str, reveal_last_chars: int = 4) -> str:
    """
    Masks sensitive value but reveals a few characters at the end for identification.
    """
    masked_value = "*" * (len(value) - reveal_last_chars) + value[-reveal_last_chars:]
    return masked_value




# DATABASE Handler
def connect_to_db(db_path: str) -> Optional[sqlite3.Connection]:
    """
    Establish a connection to the SQLite database using the provided path.
    
    Args:
        db_path (str): Path to the SQLite database file.
    
    Returns:
        A sqlite3.Connection object if a connection is successfully created, else returns None.
    """
    try:
        logging.info(f"Attempting to connect to the database: {db_path}")
        connection = sqlite3.connect(db_path)
        logging.info("Database connection successful.")
        return connection
    except sqlite3.Error as e:
        logging.error(f"Failed to connect to the database: {e}")
        return None

def close_connection(connection: Optional[sqlite3.Connection]) -> None:
    """
    Safely close the SQLite database connection.
    
    Args:
        connection: sqlite3.Connection object to be closed.
    """
    if connection:
        try:
            logging.info("Attempting to close the database connection.")
            connection.close()
            logging.info("Database connection closed successfully.")
        except sqlite3.Error as e:
            logging.error(f"Failed to close the database connection: {e}")
    else:
        logging.warning("No open connection found to close.")