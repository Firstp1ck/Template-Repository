import configparser
import logging
import os

# Set up logging
logging.basicConfig(filename='app.log', filemode='w', level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

config = configparser.ConfigParser()
config_file_path = r'config.ini' # relative path

# Function to validate file paths
def validate_file_path(path):
    if not os.path.exists(path):
        logging.error(f"File not found: {path}")
        raise FileNotFoundError(f"The required file does not exist: {path}")
    else:
        logging.info(f"File validated and exists: {path}")

if __name__ == "__main__":
    # Read and process the configuration
    try:
        if not os.path.exists(config_file_path):
            logging.error(f"Configuration file not found at {config_file_path}")
            raise FileNotFoundError(f"Configuration file not found at {config_file_path}")
        
        config.read(config_file_path)
        logging.info("Configuration file has been read successfully")

        # Retrieve paths from the config and validate each
        pdf_form = config['paths']['PDF_FORM']
        validate_file_path(pdf_form)
        print(pdf_form)

        word_form = config['paths']['WORD_FORM']
        validate_file_path(word_form)
        print(word_form)

        input_excel = config['paths']['INPUT_EXCEL']
        validate_file_path(input_excel)
        print(input_excel)

        input_db = config['paths']['INPUT_DB']
        validate_file_path(input_db)
        print(input_db)

        output = config['paths']['OUTPUT']
        validate_file_path(output)
        print(output)

    except KeyError as e:
        logging.error(f"Missing section or key in configuration file: {e}")
        raise
    except configparser.Error as e:
        logging.error(f"Error parsing the configuration file: {e}")
        raise