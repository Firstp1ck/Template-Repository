import configparser

config = configparser.ConfigParser()
config.read('config.ini')

data_dir = config['paths']['data_dir']
log_dir = config['paths']['log_dir']
db_path = config['database']['db_path']

print("Data Directory:", data_dir)
print("Log Directory:", log_dir)
print("Database Directory:", db_path)
