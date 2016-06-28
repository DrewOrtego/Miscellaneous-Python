''' loadGame.py

    Provides functionality to load a game from a save file. This takes a 
    serialized file and copies its contents into the setup.objects dict.
    This dict is utilzied by the game loop in main.py when calling
    various functions in the program.
'''

import pickle, glob, os
from gameObjects import setup

def loadPrompt():
    ''' Lists all found save files from the Saved Games directory.'''
    if os.path.exists('Saved Games'):
        save_files = {}
        for i, name in enumerate(glob.glob('Saved Games\\*.tbs'), 1):
            save_files[i] = name
        if len(save_files) == 0:
            print("No save files found in the Saved Games directory.")
        else:
            print("Please select a save file to load:\n")
            for k, v in save_files.items():
                print("  {0}: {1}".format(k, v.split('\\')[1]))
            chooseSave(save_files)
    else:  
        print("No Saved Games directory found. \
            Please save a game before loading it.")


def chooseSave(save_files):
    ''' Prompt the user to choose which save file to load and verify that it
        is a valid choice.'''
    choice = input("\nEnter a number > ")
    try:
        choice = int(choice)
    except ValueError:
        print("That's not a valid number... try again!")
    else:
        if choice not in range(1, len(save_files) + 1):
            print("Choice {0} not found, please try again.".format(choice))
        else:
            loadGame(save_files[choice])


def loadGame(file_name):
    ''' Overwrite the serialized dict to the current setup.objects dict.'''
    with open(file_name, 'rb') as f:
        saved_data = pickle.load(f)
    setup.objects = saved_data
    print("Loaded {0}".format(file_name.split('\\')[1]))

