#Example configparser:
import configparser

config = configparser.ConfigParser()
config_file_path = r'Testing\modules\config.ini' # relative path
config.read(config_file_path)

abgelaufene_schulung = config['paths']['abg_schulung']
drucken_schulung = config['paths']['dru_schulung']
aufnehmen_schulung = config['paths']['auf_schulung']

