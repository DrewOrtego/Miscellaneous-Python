''' formatOutput.py
    
    Prints output the console formatted to fit the Game object's consoleWidth
    property.

    TODO: currently hard coding the console width until the final platform
    for the game is established. (Testing is being done in Windows cmd.)
'''

import os, textwrap, math
from gameObjects import setup

def printHeader():
    ''' Prints the header showing the current room and number of moves.'''
    print("{0:<59} Moves: {1}".format(
        setup.objects['CurrentRoom'].name,
        setup.objects['Game'].completed_moves)
    )
    print('-' * 70, '\n')


def formatOutput(*message, await_input = ""):
    ''' Formats the output of an on-screen message to fit the screen width.
        Also calculates the number of rows to write on-screen and ensure that
        the prompt is always in the same place.
        <Press any button to continue> functionality can be achieved by 
        sending a string to the await_input parameter.'''
    #input() # DBUG allows tester to see any messages being overwritten
    os.system('cls')
    printHeader()
    message_length = 0
    for m in message:
        message_length += len(m)
        split_msg = " ".join(m.split())
    rows = math.ceil(message_length/70)
    print(textwrap.fill(split_msg, 70)) # Hard code width for now
    for r in range(1, 10-rows):
        print('')
    if await_input != "":
        input(await_input)