''' saveGame.py

    Allows the player to save the current game state to a file. Prompts the user
    for a file name and verifies that the file name does not already exist. If 
    so, the file will not be saved.
'''

import os, pickle, glob
from userInterface.formatOutput import formatOutput as print

def savePrompt(objects):
    ''' Save a serialized copy of the setup.objects dict to a file.'''
    file_name = input("Enter a file name > ")
    file_name += '.tbs'
    if fileExists(file_name):
        print("File already exists! Specify a unique name when saving.")
    else:
        saveGame(file_name, objects)


def fileExists(file_name):
    ''' Verify that the speified file name doesn't already exist before 
    saving. Returns True if the file name does not already exist.'''
    for name in glob.glob('Saved Games\\*.tbs'):
        if file_name.lower() == name.split('\\')[1].lower():
            return True
    return False


def saveGame(file_name, objects):
    ''' Save the game file to the 'Saved Games' directory.'''
    if not os.path.exists('Saved Games'):
        os.makedirs('Saved Games')
    with open(os.path.join('Saved Games', file_name), 'wb') as f:
        pickle.dump(objects, f)

    if os.path.exists(os.path.join('Saved Games', file_name)):
        print("Game saved as {0}".format(file_name))
    else:
        print("Unknown error encountered when saving file {0}".format(\
            file_name))
    
        