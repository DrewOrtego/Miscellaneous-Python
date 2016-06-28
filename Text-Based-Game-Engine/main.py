''' main.py
    
    Contains the message which prints to the console at the start of a new game,
    and the main game loop. No objects should be created here. Only high level 
    logic which controls the start and end of a turn/move should be written 
    here.
'''

from gameObjects import setup
from commandProcessing import tokenizer, processInput, interface
from userInterface.formatOutput import formatOutput as print

def getObjects():
    ''' Returns the dict with all in-game objects. This dict should read upon 
        each iteration of the game loop to allow for overwriting the dict using 
        the load functionality.''' 
    return setup.objects


def gameLoop(objects):
    ''' Main game loop. Executes while the Actor is still alive.
        Get the user's input, create tokens out of it, and process it.'''    
    user_input = [word for word in input(objects['Game'].prompt_char).split()]
    if user_input:
        tokenized_input = tokenizer.get_token(user_input)
        if 'unknown_word' not in tokenized_input[0].keys():
            valid_pattern = tokenizer.pattern_match(tokenized_input)
            if valid_pattern:
                processInput.executeCommand(tokenized_input, 
                    valid_pattern, objects)
            else:
                print("I didn't understand that sentence.")
        else:
            print("I don't recognize the word {0}.".format(
                tokenized_input[0]['unknown_word']))
    else:
        print("Pardon?")


if __name__ == "__main__":
    ''' Loads the objects dict from setup to begin the loop, and loads it 
        again once the loop begins. This allows the load functionality to
        work properly as the game loops.'''
    objects = getObjects()
    objects['CurrentRoom'].look(objects)
    while(objects['Actor'].dead == False):
        objects = getObjects()
        gameLoop(objects)

