#Example configparser:
import configparser
import logging
import os

# Set up logging
logging.basicConfig(filename='app.log', filemode='w', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

def get_base_path() -> str:
    """Get the base path of the project directory."""
    return os.path.dirname(os.path.abspath(__file__))

def get_config_path() -> str:
    """Get the absolute path of the config.ini file."""
    config_path = os.path.join(get_base_path(), 'config.ini')
    logging.debug(f"Config path: {config_path}")
    return config_path

def load_config() -> configparser.ConfigParser:
    """Load the configuration file."""
    config = configparser.ConfigParser()
    config_path = get_config_path()
    if not os.path.exists(config_path):
        logging.error(f"Configuration file not found at: {config_path}")
        raise FileNotFoundError(f"Configuration file not found at: {config_path}")
    config.read(config_path)
    logging.info("Configuration file has been read successfully")
    return config

def resolve_and_validate_path(key: str, config: configparser.ConfigParser) -> str:
    """Resolve and validate the path from the configuration."""
    try:
        relative_path = config['paths'][key]
        absolute_path = os.path.join(get_base_path(), relative_path)
        if not os.path.exists(absolute_path):
            logging.error(f"The required file does not exist: {absolute_path}")
            raise FileNotFoundError(f"The required file does not exist: {absolute_path}")
        logging.info(f"File validated and exists: {absolute_path}")
        return absolute_path
    except KeyError:
        logging.error(f"Missing key '{key}' in 'paths' section of configuration")
        raise

try:
    config = load_config()
    pdf_form_path = resolve_and_validate_path('PDF_FORM', config)
    word_form_path = resolve_and_validate_path('WORD_FORM', config)
    input_excel_path = resolve_and_validate_path('INPUT_EXCEL', config)
    input_db_path = resolve_and_validate_path('INPUT_DB', config)
    output_path = resolve_and_validate_path('OUTPUT', config)

except Exception as e:
    logging.exception("An error occurred while processing the file paths.")
