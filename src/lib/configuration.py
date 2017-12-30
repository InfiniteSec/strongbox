# Necessary imports

import configparser
import os
from uuid import uuid4


class Config:

    # Config file location
    configPath = None
    c = configPath
    # Config
    config = configparser.ConfigParser()

    def __init__(self, c):
        self.c = c

    # Returns a user config and sets a default, if necessary.
    def get_config(self):
        # Generates a default config file for the first time
        if not os.path.isfile(self.c):
            self.set_default_config_file()

        # Loads an existing config file
        self.config.read(self.c)
        return self.config['MAIN']

    # Sets a user's default config file
    def set_default_config_file(self):
        self.config['MAIN'] = {

            'version': '1.00',
            'keyVersion': '1',
            'salt': self.generate_random_salt(),
            'clipboardTime': '20',
            'hideSecretTime': '7',
            'autoLockTime:': '600',
        }

        # Saves config file
        self.save_config()

    # Updates a config value
    def update(self, name, value):
        # Sets a new value
        self.config['MAIN'][name] = str(value)

        # Saves updated config value
        self.save_config()

        print(' ')
        print('[+] The setting %s` is now set to %s`.' % (name, value))
        print(' ')

    # Saves a user config to their designated config file
    def save_config(self):
        with open(self.c, 'w') as configFile:
            self.config.write(configFile)
        os.chmod(self.c, 0o600)

    # Generates a random salt to strength password generation
    def generate_random_salt(self):
        # This will be used to generate the StrongBox hash w/ the User's Secret Key
        return str(uuid4())
