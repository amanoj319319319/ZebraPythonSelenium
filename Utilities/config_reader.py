# utilities/config_reader.py
import configparser
import os

config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.ini')
config.read(config_path)

def get_base_url():
    return config['DEFAULT']['base_url']

def get_valid_credentials():
    return config['credentials_valid']['username'], config['credentials_valid']['password']

def get_invalid_credentials():
    return config['credentials_invalid']['username'], config['credentials_invalid']['password']
