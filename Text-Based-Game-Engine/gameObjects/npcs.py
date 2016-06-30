''' NPCs.py

    Contains all non-playable characters
'''

from gameObjects import events
from userInterface.formatOutput import formatOutput as print

class NPC:
    def __init__(self):
        ''' The parent class for all npc objects'''
        self.accept_items = [] # List of items the NPC can take
        self.give_events = {} # Select-case for actions to occur once a specific
            # item is given to the NPC.
        self.name = ['<name goes here>']
        self.visible = False # True mentions NPC in the look command


    def ask(self, objects, noun=None):
        print("{0} doesn't seem to have much to say about that.".format(\
            self.name[0]))


    def ask_about(self, noun):
        self.ask(noun)


    def ask_for(self, noun):
        self.ask(noun)


    def give(self, item_obj, objects):
        ''' Give an item to a NPC. Availability of both is checked in
            processInput.py'''
        if item_obj.__class__.__name__ in self.accept_items:
            objects['Inventory']['Actor'].remove(item_obj)
            objects['Inventory'][self.__class__.__name__].append(item_obj)
            print('''You have given {0} the {1}.'''.format(
                self.name, item_obj.name))
        else:                
            print('''{0} doesn't seem to want the {1}.'''.format(
                self.name[0], item_obj.name))


    def hug(self, objects):
        print('''"Huh?"''')


    def kiss(self, objects):
        print('''"Huh?"''')


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
        self.accept_items = ['Card'] # List of items the NPC can take
        self.description = 'Drew appears to have a deep affinity for t-shirts.'
        self.give_events = {
            'Card': self.get_card
        }
        self.has_card = False
        self.name = ['Drew']
        self.visible = True


    def get_card(self, objects):
        ''' Actions to occur after giving Drew the card.'''
        print('''"Whoa, this card is sick brah! I can't just take it from you
            though, it's too expensive. I can appreciate you trying to figure
            out who it belongs to though. Let me see if I can help you out."''')


    def hug(self, objects):
        print('''"Please stop squeezing me with your body."''')


    def kiss(self, objects):
        print('''"I'm just gonna pretend that didn't happen."''')


    def give(self, item_obj, objects):
        ''' Give an item to a NPC. Availability of both is checked in
            processInput.py'''
        if item_obj.__class__.__name__ in self.accept_items:
            objects['Inventory']['Actor'].remove(item_obj)
            objects['Inventory'][self.__class__.__name__].append(item_obj)
            try:
                self.give_events[item_obj.__class__.__name__](objects)
            except KeyError:
                print('''You have given {0} the {1}.'''.format(
                self.name, item_obj.name))
        else:                
            print('''"I don't have any need for that thing, 
                you can keep it."'''.format(self.name, item_obj.name))

