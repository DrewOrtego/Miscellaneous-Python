''' commands.py

    Contains all valid commands in the game. This module is utilized by the
    Tokenizer module when determining whether a command is valid or not.

    Each set of commands are associated with a token, which will examine the 
    name of the tuple containing the command to determine which type of token
    to associate with a command.

    This module should contain all valid commands, and each command should be 
    reserved to one action, room, or item. "Command overloading" should be 
    avoided, unless a command is utilized as an adverb for multiple items. The 
    Tokenizer module will examine a specific item's adverbs to check for 
    validity, and this will bypass any confusion with tokenizing a word which 
    is used in more than one instance. That should be safe, I think...
'''

verbs = (
    # Actions that can be performed with items.
    
    # A --------------------------------
    'ask',

    # C --------------------------------
    'close', 'cut',

    # D --------------------------------
    'drop',

    # E --------------------------------
    'eat', 'enter', 'examine', 'exit',

    # G --------------------------------
    'give',
    
    # H --------------------------------
    'hit', 'hug',
    
    # K --------------------------------
    'kiss',

    # L --------------------------------
    'l', 'look',

    # M --------------------------------
    'move',

    # O --------------------------------
    'open',

    # P --------------------------------
    'place', 'put',

    # R --------------------------------
    'r', 'read', 'remove',
    
    # S --------------------------------
    'slice',

    # T --------------------------------
    'take', 'throw',
    
    # U --------------------------------
    'use',

    # X --------------------------------
    'x',
    )

nouns = (
    # Items that used for interactions.

    # B --------------------------------
    'booster',

    # C --------------------------------
    'card',

    # D --------------------------------
    'door',

    # T --------------------------------
    'table',

    # J --------------------------------
    'jace',

    # P --------------------------------
    'pack',

    # R --------------------------------
    'resume',
    )

directions = (
    # Directions and their shortcuts
    'north', 'east', 'south', 'west', 'n','e','s','w',
    'northeast', 'southeast', 'southwest', 'northwest', 'ne','se','sw','nw',
    'up', 'down', 'u', 'd',
    )

interface = (
    # Commands stored in the game module.

    # B --------------------------------
    'b', 'brief',

    # H --------------------------------
    'h', 'help',

    # I --------------------------------
    'i', 'inventory',

    # L --------------------------------
    'load',

    # M --------------------------------
    'moves',

    # P --------------------------------
    'prompt',

    # S --------------------------------
    'save',
    
    # Q --------------------------------
    'quit',

    # V --------------------------------
    'v', 'verbose',
    )

combine = (
    # Verbs used in conjuntion with other verbs, and using two items.

    # A --------------------------------
    'about',

    # F -------------------------------
    'for', 'from',

    # I --------------------------------
    'in', 'inside',
    
    # O --------------------------------
    'on',
    )

preposition = (
    # Commands that are ignored; parsed out of a valid phrase.

    # A --------------------------------
    'a', 'at',

    # T --------------------------------
    'the',
    )

adjectives = ( 
    # Used to descibe items (e.g. take the small pawn)
    # Found in the 'adjective' attribute of an item.

    # B --------------------------------
    'booster',

    # G --------------------------------
    'glass',

    # I --------------------------------
    'ikea',
    
    # J --------------------------------
    'jace',

    # L --------------------------------
    'large',

    # M --------------------------------
    'magic',
    )

npcs = (
    # Names of all non-playable characters

    # D --------------------------------
    'drew',
    )

