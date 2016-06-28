''' Game.py
'''

from userInterface.formatOutput import formatOutput as print

class Game:
    def __init__(self):
        self.brief_msg = False
        self.completed_moves = 0
        self.console_width = 70
        self.current_room = None
        self.prompt_char = "\n> "
        self.tutorial_mode = None
        self.verbose_msg = True

            
    def print_header(self):
        ''' Prints the current room's name and number of moves.'''
        move_msg = "moves: " + str(self.moves)
        spaces = self.console_width -len(self.current_room.name) -len(move_msg)
        print(); print()
        print(self.current_room.name + (" " * spaces) + move_msg)
        print("-" * self.console_width)
    
        
    def tutorial_choice(self):
        print('''Welcome to the game demo! If you haven't played this
            before then there are a few things you'll need to know. If you have
            played before then you can totally skip this intro stuff.''')
        while self.tutorial_mode == None:
            prompt = input('''Have you played this game before? (y/n) ''' + \
                self.prompt_char)
            if prompt.lower() in ['yes', 'y']:
                self.tutorial_mode = False
            elif prompt.lower() in ['no', 'n']:
                self.tutorial_mode = True
            else:
                print('''I didn't understand your input. Type 'yes' or 
                    'no' and press Enter.''')
        
    def win(self):
        print("Congrats! You've completed the game!")
        raise SystemExit

        
