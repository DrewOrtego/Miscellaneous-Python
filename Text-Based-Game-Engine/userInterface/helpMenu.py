''' Help.py

    The interactive help menu which can be accessed in-game at any time.
'''

import os, textwrap 
from collections import OrderedDict as OD


def about():
    ''' Prints message about the game and text-based gaming in general.'''
    message = """You are currently playing a text-based game.
Specifically, you're in the help menu for said game. Text-based
games were really popular back in the early 80's, but then graphics
came out and that was the end of that. I wish I could say that
text-based games are making a come back, but they're not. However,
they're a lot of fun to make, and this one tries to by fun to play,
as well as maintain. Check out option 2 for some more details on
how to play this game, and thanks for giving it a try!"""
    print('\n'.join(textwrap.wrap(message, 70)))
    print('\n')
    input('Press any key to continue...')


def commands():
    message = '''The following case-insensitive commands are available,
and most have one or two-letter shortcuts you can try and find.
This is not the complete list of commands; there are many more for
you to discover.'''
    print('\n'.join(textwrap.wrap(message, 70)))
    print('\n')

    print("DIRECTIONS")
    message = '''North (or N), East, South, West, Northeast (or NE), 
Southeast, Southwest, Northwest, up or climb, down, enter, exit.'''
    print('\n'.join(textwrap.wrap(message, 70)))
    print('\n')

    print("COMMON VERBS")
    print("Close, Look, Open, Read, Take, Use.\n")

    print("INTERFACE")
    print("Brief, Help, Inventory, Load, Moves, Prompt, Save, \
        Quit, Verbose.\n")

    print("ITEM COMMANDS")
    print("Use item_1 with item_2, Place/Put item_1 In/On/Inside \
        item_2, Ask item_1 About item_2, Remove item_1 From item_2\n")

    print("IGNORED WORDS")
    print('''A, At, The.''')
    print('\n')
    input('Press any key to continue...')
    

def instructions():
    message ='''This game reads your input and tells you a) whether it
understands your input, or b) what has happened in the game because
of what you've entered for input. Most of the valid patterns 
consist of a direction, a noun and/or a verb, or an adverb which 
allows you to perform special actions with items in the game.'''
    print('\n'.join(textwrap.wrap(message, 70)))
    print('\n')
    message = '''The best way to figure out how to interact with your 
environment is to read the list of valid commands from the help 
menu (item 3), and carefully read the details of each room you 
enter. Details about a room will tell you what items are in that 
room, and give you ideas about what you can do in that room. For 
instance, if you enter a room and see the following...'''
    print('\n'.join(textwrap.wrap(message, 70)))
    print('\n')
    print("The walls in this room are covered in gross slime.")
    message = '''...then typing "wall", "walls", "slime", or "gross
slime" will probably tell you something about those objects. Typing 
"kiss slime" will probably make you gag but then tell you something 
about the results of that action. Sometimes those results are 
useful, sometimes they are just plain hilarious, and sometimes they 
kill you, so get ready for that!'''
    print('\n'.join(textwrap.wrap(message, 70)))
    print('\n')
    input('Press any key to continue...')
    

def print_title():
    ''' Print the title of the main menu.'''
    header = 'Help Topics'
    stars = '-' * ((35) - len(header) + 1)
    print(stars, header, stars)


def quit():
    ''' Nothing to see here.'''
    pass


def menu_loop():
    ''' Prompts the user to select a menu item.'''
    menu = OD()
    menu['1'] = 'About This Game'
    menu['2'] = 'How to Play'
    menu['3'] = 'Valid Commands'
    menu['4'] = 'Exit the Help Menu'

    functions = {
        '1' : about,
        '2' : instructions,
        '3' : commands,
        '4' : quit,
    }

    quit_help = False

    os.system('cls')
    while(quit_help == False):
        print_title()
        for k, v in menu.items(): print('  ', k, ':', v)
        choice = input('> ')
        print('\n')
        if choice not in (menu.keys()):
            os.system('cls')
            print('That\'s not a choice... let\'s try this again...')
            print('\n')
        elif choice == '4': # player has chosen to quit the help menu
            quit_help = True
            os.system('cls')
        else:
            functions[choice]()
            os.system('cls')

