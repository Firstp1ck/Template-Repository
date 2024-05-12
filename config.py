import configparser

config = configparser.ConfigParser()
config.read('config.ini')

data_dir = config['paths']['data_dir']
log_dir = config['paths']['log_dir']

print("Data Directory:", data_dir)
print("Log Directory:", log_dir)
