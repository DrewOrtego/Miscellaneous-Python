''' actor.py
'''

from userInterface.formatOutput import formatOutput as print

class Actor:
    
    def __init__(self):
        self.dead = False
        self.inventory = ""
        self.win = False


    def game_over(self, message):
        print(message, await_input = "\nGame Over!")
        raise SystemExit