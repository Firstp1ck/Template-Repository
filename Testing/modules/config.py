#Example configparser:
import configparser
import logging
import os

# Set up logging
logging.basicConfig(filename='app.log', filemode='w', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

config = configparser.ConfigParser()
config_file_path = r'Prod\config.ini' # relative path

# Function to validate file paths
def validate_file_path(path):
    if not os.path.exists(path):
        logging.error(f"File not found: {path}")
        raise FileNotFoundError(f"The required file does not exist: {path}")
    else:
        logging.info(f"File validated and exists: {path}")

# Read and process the configuration
try:
    if not os.path.exists(config_file_path):
        logging.error(f"Configuration file not found at {config_file_path}")
        raise FileNotFoundError(f"Configuration file not found at {config_file_path}")
    
    config.read(config_file_path)
    logging.info("Configuration file has been read successfully")

    # Retrieve paths from the config and validate each
    vorlage_form_1773_pfad = config['paths']['form_1773']
    validate_file_path(vorlage_form_1773_pfad)

    vorlage_form_1778_pfad = config['paths']['form_1778']
    validate_file_path(vorlage_form_1778_pfad)

    avl_pvl_pfad = config['paths']['AVL_PVL']
    validate_file_path(avl_pvl_pfad)

    pdf_save = config['paths']['PDF_SAVE']
    validate_file_path(pdf_save)

    pdf_input = config['paths']['PDF_INPUT']
    validate_file_path(pdf_input)    

except KeyError as e:
    logging.error(f"Missing section or key in configuration file: {e}")
    raise
except configparser.Error as e:
    logging.error(f"Error parsing the configuration file: {e}")
    raise
