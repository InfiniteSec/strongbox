def emblem():
    """
    StrongBox; your solution to protect your sensitive passwords and information, brought to you by Infinite Security.
    """
    print(r"   ____  _                         ____             ")
    print(r"  / ___\| |                       |  _ \            ")
    print(r" | (___ | |_ _ __ ___  _ __   __ _| |_) | _____  __ ")
    print(r"  \___ \| __| '__/ _ \| '_ \ / _` |  _ < / _ \ \/ / ")
    print(r" ____)  | |_| | | (_) | | | | (_| | |_) | (_) >  <  ")
    print(r" \_____/ \__|_|  \___/|_| |_|\__, |____/ \___/_/\_\ ")
    print(r"                              __/ |                 ")
    print(r"                             |___/                  ")
    print(r"     StrongBox 1.0                                  ")
    print(r"                             By: Infinite Security  ")


def mkfolder_if_missing(folder_path):
    # import local
    import os

    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    except Exception as e:
        import sys

        print(" ")
        print("[-] Unable to create the folder `%s`. This folder stores the StrongBox and config file.' % folder_path.")
        print("    >>> Please make sure to verify your permissions.                                                   ")
        print("    >>> Otherwise, run ./strongbox.py --help to learn how to select an alternative path for both files.")
        print(" ")
        sys.exit()


# Verifies that StrongBox && its config file both exist
def assess_integrity(sb_path, conf_path):
    """
    The vault config file contains a salt. The salt is used to unlock the vault along with the Secret Key.
    Config files are created automatically. This is a default setting of StrongBox. New config files do NOT
    allow a user to open an existing StrongBox. This function verifies that both a config file and a StrongBox exist.
    """
    # import local
    import os
    import sys

    if not os.path.isfile(conf_path) and os.path.isfile(sb_path):
        print("                                                                                                     ")
        print("[-] Uh oh! The StrongBox is set up but your config file is missing...                                ")
        print("   For your security, the StrongBox cannot unlocked without a critical component of the config file. ")
        print("                                                                                                     ")
        print("    >>> Please restore the config file before proceeding.                                            ")
        print("       You are missing the salt, a vital component that is required to access your StrongBox.        ")
        print("                                                                                                     ")
    sys.exit()


# User confirmation required; initiates StrongBox purge_sb method; permanently erases the StrongBox and its config file
def purge_sb(sb_path, conf_path):
    # import local
    import os
    import sys

    print(' ')
    if confirm_response(prompt='Are you sure you wish to purge your? ALL data will be lost forever.', response=False):
        # Perform Self-Destruct Sequence
        if os.path.isfile(conf_path):
            os.remove(sb_path)
        if os.path.isfile(conf_path):
            os.remove(conf_path)

        print('                                              ')
        print('[+] ACTION SUCCESSFUL. YOUR STRONGBOX HAS BEEN')
        print('    >>> The StrongBox and conf file           ')
        print('            have been DELETED.                ')
        print('                                              ')
        sys.exit()
    else:
        sys.exit()


def confirm_response(ask=None, response=False):

    # SOURCE: http://code.activestate.com/recipes/541096-prompt-the-user-for-confirmation/

    """
    Small custom changes have been made to this src code and it has been adapted to Python3.
    # Prompts for a response from the User. Returns True for yes and False for no.
    # 'response' should be set to the default value assumed by the caller when user simply types ENTER.

    >>> confirm(ask='Create Directory?', response=True)
    Create Directory? [y]|n:
    True
    """

    if ask is None:
        ask = 'Confirm'

    if response:
        ask = '%s [Y/n]: ' % ask
    else:
        ask = '%s [y/N]: ' % ask

    while True:
        answer = input(ask)
        if not answer:
            return response
        if answer not in ['y', 'Y', 'n', 'N']:
            print('please enter y or n.')
            continue
        if answer == 'y' or answer == 'Y':
            return True
        if answer == 'n' or answer == 'N':
            return False
