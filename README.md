PROJECT IS NOT DONE. PLEASE DO NOT ATTEMPT TO INSTALL.
DO NOT FOLLOW THE INSTALLATION DIRECITONS IN THIS README FILE

# PLEASE NOTE THIS SECTION IS NOT DONE. WILL EDIT AND BE DONE SOON.

StrongBox is a project that build off of vault.py
SOURCE: https://github.com/gabfl/vault

StrongBox is an anti-forensics security tool; a highly secure CLI Password and Information Manager coded in Python3.

Features

    AES-256 encryption with pyocryptodome
    Secret key is hashed with a unique salt (100,000 iterations)
    Possibility to create an unlimited number of StrongBoxes
    Clipboard cleared automatically
    Automatic vault locking after inactivity
    Automatic password generator that generates "Fort Knox Passwords"
    Import / Export in Json
    Self-Destruct/Purge feature for anti-forensics

# DO NOT DO ANY OF THE FOLLOWING UNTIL PROJECT IS COMPLETE
Basic usage

Installation and setup
Using PyPI

pip3 install strongbox

# Run setup
strongbox

Cloning the project

# Clone project
git clone https://github.com/infinitesec/strongbox && cd strongbox

# Installation
python3 setup.py install

# Run setup
vault

Advanced settings:

usage: vault [-h] [-t [CLIPBOARD_TTL]] [-p [HIDE_SECRET_TTL]]
             [-a [AUTO_LOCK_TTL]] [-v VAULT_LOCATION] [-c CONFIG_LOCATION]
             [-k] [-i IMPORT_ITEMS] [-x EXPORT] [-f [{json,native}]] [-e]

optional arguments:
  -h, --help            show this help message and exit
  -t [CLIPBOARD_TTL], --clipboard_TTL [CLIPBOARD_TTL]
                        Set clipboard TTL (in seconds, default: 15)
  -p [HIDE_SECRET_TTL], --hide_secret_TTL [HIDE_SECRET_TTL]
                        Set delay before hiding a printed password (in
                        seconds, default: 15)
  -a [AUTO_LOCK_TTL], --auto_lock_TTL [AUTO_LOCK_TTL]
                        Set auto lock TTL (in seconds, default: 900)
  -v VAULT_LOCATION, --vault_location VAULT_LOCATION
                        Set vault path
  -c CONFIG_LOCATION, --config_location CONFIG_LOCATION
                        Set config path
  -k, --change_key      Change master key
  -i IMPORT_ITEMS, --import_items IMPORT_ITEMS
                        File to import credentials from
  -x EXPORT, --export EXPORT
                        File to export credentials to
  -f [{json,native}], --file_format [{json,native}]
                        Import/export file format (default: 'json')
  -e, --erase_vault     Erase the vault and config file
## PLEASE NOTE THIS SECTION IS NOT DONE. WILL EDIT AND BE DONE SOON.

StrongBox is a project that build off of vault.py
Source: https://github.com/gabfl/vault

StrongBox is an anti-forensics security tool; a highly secure CLI Password and Information Manager coded in Python3.

Features

    AES-256 encryption with pycryptodome
    Secret key is hashed with a unique salt (100,000 iterations)
    Possibility to create an unlimited number of StrongBoxes
    Clipboard cleared automatically
    Automatic vault locking after inactivity
    Password suggestions with password-generator-py
    Import / Export in Json
    Self-Destruct/Purge StrongBox for secure anti-forensics

Basic usage

Installation and setup
Using PyPI

pip3 install strongbox

# Run setup
strongbox

Cloning the project

# Clone project
git clone https://github.com/infinitesec/strongbox && cd strongbox

# Installation
python3 setup.py install

# Run setup
vault

Advanced settings:

usage: vault [-h] [-t [CLIPBOARD_TTL]] [-p [HIDE_SECRET_TTL]]
             [-a [AUTO_LOCK_TTL]] [-v VAULT_LOCATION] [-c CONFIG_LOCATION]
             [-k] [-i IMPORT_ITEMS] [-x EXPORT] [-f [{json,native}]] [-e]

optional arguments:
  -h, --help            show this help message and exit
  -t [CLIPBOARD_TTL], --clipboard_TTL [CLIPBOARD_TTL]
                        Set clipboard TTL (in seconds, default: 15)
  -p [HIDE_SECRET_TTL], --hide_secret_TTL [HIDE_SECRET_TTL]
                        Set delay before hiding a printed password (in
                        seconds, default: 15)
  -a [AUTO_LOCK_TTL], --auto_lock_TTL [AUTO_LOCK_TTL]
                        Set auto lock TTL (in seconds, default: 900)
  -v VAULT_LOCATION, --vault_location VAULT_LOCATION
                        Set vault path
  -c CONFIG_LOCATION, --config_location CONFIG_LOCATION
                        Set config path
  -k, --change_key      Change master key
  -i IMPORT_ITEMS, --import_items IMPORT_ITEMS
                        File to import credentials from
  -x EXPORT, --export EXPORT
                        File to export credentials to
  -f [{json,native}], --file_format [{json,native}]
                        Import/export file format (default: 'json')
  -e, --erase_vault     Erase the vault and config file
