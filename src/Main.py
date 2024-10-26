import configparser
import logging
import os
import modules as m

def main():
    # Set up logging
    m.setup_logging()

    config = configparser.ConfigParser()
    config_file_path = r'src\config.ini' # relative path

    m.load_environment_variables()
    required_env_vars = ['API_KEY', 'DATABASE_URL', 'SECRET_KEY']

    # Fetch multiple environment variables
    env_vars = m.get_multiple_env_variables(required_env_vars)

    # Log the result
    if all(env_vars.values()):  # only if all required env vars are present and not empty
        print(f"API Key: {m.mask_sensitive_value(env_vars['API_KEY'])}")
        print(f"Database URL: {env_vars['DATABASE_URL']}")
        print(f"Secret Key: {m.mask_sensitive_value(env_vars['SECRET_KEY'])}")
    else:
        logging.error("One or more environment variables are missing. Please check them.")

    # Read and process the configuration
    try:
        if not os.path.exists(config_file_path):
            logging.error(f"Configuration file not found at {config_file_path}")
            raise FileNotFoundError(f"Configuration file not found at {config_file_path}")
        
        config.read(config_file_path)
        logging.info("Configuration file has been read successfully")

        # Define the keys to validate
        path_keys = ['PDF_FORM', 'WORD_FORM', 'INPUT_EXCEL', 'INPUT_DB', 'OUTPUT']

        # Validate paths and print them
        m.validate_and_print_paths(config, 'paths', path_keys)

    except KeyError as e:
        logging.error(f"Missing section or key in configuration file: {e}")
        raise
    except configparser.Error as e:
        logging.error(f"Error parsing the configuration file: {e}")
        raise

        # Retrieve the database path
    db_path = config['paths'].get('INPUT_DB')

    if db_path:
        # Connect to the database
        connection = m.connect_to_db(db_path)
        
        if connection:
            # Perform database operations...
        
            # Close the database once done
            m.close_connection(connection)
        else:
            print("Failed to connect to the database.")
    else:
        print("Database path not found in configuration.")

if __name__ == "__main__":
    main()