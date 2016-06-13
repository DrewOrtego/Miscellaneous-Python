''' Interface.py

    All commands used in interacting with the interface of the game. (i.e. 
    mainipulates the console.) Note the lack of a class here.
'''

from saveLoad import loadGame, saveGame
from userInterface import helpMenu
import textwrap, os, pickle
from pprint import pprint
from userInterface.formatOutput import formatOutput as print

COPYRIGHT = ''' Text-based Game Demo v.1.0: The Fundamentals'''

def b(objects):
    ''' Shortcut to brief.'''
    brief(objects)


def brief(objects):
    ''' Activates brief descriptions for rooms. Deactivates verbose
        descriptions.'''
    if objects['Game'].brief_msg:
        print("Brief descriptions are already activated.")
    else:
        objects['Game'].brief_msg = True
        objects['Game'].verbose_msg = False
        print("Brief descriptions are now on.")


def h(objects):
    ''' Shortcut to help.'''
    help(objects)


def help(objects):
    ''' Prints a list of available commands.'''
    helpMenu.menu_loop()
    look(objects)
         

def i(objects):
    ''' Shortcut to the "inventory" command.'''
    inventory(objects)
    

def inventory(objects):
    ''' Formats and prints the current items in the actor's inventory.'''
    if objects['Inventory']['Actor'] == []:
        print("You don't have anything in your inventory.")
    else:
        item_list = [i for i in objects['Inventory']['Actor']]
        message = "You are currently carrying "
        for i in item_list:
            message += "a {}".format(i.name[0])
            if item_list.index(i) + 1 == len(item_list):
                message += "."
            elif item_list.index(i) + 2 == len(item_list):
                message += ", and "
            else:
                message += ", "
        print(message)
        

def l(objects):
    ''' Shortcut for the "look" command.'''
    self.look(objects)


def load(objects):
    ''' Loads a game state from a save file.'''
    loadGame.loadPrompt()


def look(objects):
    ''' Prints the current room's description, and any available items.'''
    msg = objects['CurrentRoom'].description
    room_class = objects['CurrentRoom'].__class__.__name__
    for i in objects['Inventory'][room_class]:
        if i.visible:
            msg += (' There is a {} here.'.format(i.name[0]))
        if i.contains_item:
            stored_item = objects['Inventory'][room_class]
            if stored_item.visible:
                msg += (' There is a {} inside the {}.'.format(\
                    stored_item.name[0],
                    i.name[0]))
    print(msg)


def moves(objects):
    ''' Displays the number of successful moves that have been made.'''
    print("You have executed {} valid commands.".format(\
        objects['Game'].completed_moves))


def prompt(new_prompt = ""):
    ''' Creates a new prompt to precede the user's input. Updates the 
        "prompt_char" attribute of the game object.'''
    if new_prompt == "":
        new_prompt = input("Type a new prompt and press <Enter>: ")
    self.prompt_char = "\n" + new_prompt + " "

    
def save(objects):
    ''' Calls the saveGame module to save the current state of the game.'''
    saveGame.savePrompt(objects)


def v(objects):
    ''' Shortcut to verbose.'''
    verbose(objects)


def verbose(objects):
    ''' Activates verbose descriptions for rooms. Deactivates brief
        descriptions.'''
    if objects['Game'].verbose_msg:
        print("Verbose is already on.")
    else:
        objects['Game'].brief_msg = False
        objects['Game'].verbose_msg = True
        print("Maximum verbosity.")


def quit(objects):
    ''' Prompts user for verification to exit the game.'''
    prompt = input("Are you sure you want to quit? " + objects['Game'].prompt_char)
    if prompt.lower() == 'yes' or prompt.lower() == 'y':
        print ("It's game over, man! GAME OVER!!\n")
        raise SystemExit
    else:
        print ("OK, nevermind then.")

