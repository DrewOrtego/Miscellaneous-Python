''' NPCs.py

    Contains all non-playable characters
'''

from gameObjects import events
from userInterface.formatOutput import formatOutput as print

class NPC:
    def __init__(self):
        ''' The parent class for all item objects in the '''
        self.name = ['<name>']
        self.accept_items = [] # List of items the NPC can take
        self.visible = False # True alerts player to presence of NPC using look


    def ask(self, objects, noun=None):
        print("{0} doesn't seem to have much to say about that.".format(\
            self.name[0]))


    def ask_about(self, noun):
        self.ask(noun)


    def ask_for(self, noun):
        self.ask(noun)


    def give(self, objects):
        #1 Is item available for you to give?
        available_items = [
            i for i 
            in objects['Inventory'][objects['CurrentRoom'].__class__.__name__]
            and objects['Inventory']['Actor']
        ]
        for i in available_items:
            if i in self.accept_items:
                print('''{0} can accept the {1}'''.format(i, self.name))
            else:                
                print('''{0} cannot accept the {1}'''.format(i, self.name))
        #2 Can NPC accept this item?

        #3 Add item to NPC's 


    def hug(self, objects):
        print('''"Please stop squeezing me with your body."''')


    def kiss(self, objects):
        print('''"I'm just gonna pretend that didn't happen."''')


    def l(self, objects):
        self.look(objects)


    def look(self, objects):
        print(self.description)


    def examine(self, objects):
        self.first_examine = False
        print('''"What are you staring at?"''')


    def x(self, objects):
        self.examine(objects)


class Drew(NPC):
    def __init__(self):
        NPC.__init__(self)
        self.description = ''
        self.accept_items = ['Card'] # List of items the NPC can take
        self.name = ['Drew']
        self.visible = True

