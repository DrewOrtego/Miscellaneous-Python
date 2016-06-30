''' NPCs.py

    Contains all non-playable characters
'''

from gameObjects import events
from userInterface.formatOutput import formatOutput as print

class NPC:
    ''' Base class for all non-playable characters in the game.'''
    def __init__(self):
        self.accept_items = [] # List of items the NPC can take
        self.give_events = {} # Select-case for actions to occur once a specific
            # item is given to the NPC.
        self.name = ['<name goes here>']
        self.take_items = {}
        self.talk_subjects = {}
        self.visible = False # True mentions NPC in the look command


    def ask(self, objects, noun=None):
        print("{0} doesn't seem to have much to say about that.".format(\
            self.name[0]))


    def ask_about(self, noun):
        self.ask(noun)


    def ask_for(self, noun):
        self.ask(noun)


    def examine(self, objects):
        self.first_examine = False
        visible_items = [
            i for i in objects['Inventory'][self.__class__.__name__] 
            if i.visible
        ]
        msg = None
        for i in visible_items:
            # For 1 item
            if i.visible and len(visible_items) == 1:
                msg = ('{0} has a {1}.'.format(self.name[0], i.name[0]))

            # For 2 items
            elif i.visible and len(visible_items) == 2:
                if visible_items.index(i) == 0:
                    msg = ('{0} has a {1}, '.format(i.name[0]))
                else: 
                    msg += ('and a {0}.'.format(i.name[0]))

            # For more than 2 items
            elif i.visible and len(visible_items) > 1:
                if visible_items.index(i) == 0:
                    msg = ('{0} has a {1}, '.format(i.name[0]))
                elif visible_items.index(i) != len(visible_items) - 1:
                    msg += (' a {0}, '.format(i.name[0]))
                else:
                    msg += (' and a {0}.'.format(i.name[0]))
        if msg == None:
            print('''{0} doesn't appear to have anything of interest.'''.format(
                self.name[0]))
        else:
            print(msg)


    def give(self, item_obj, objects):
        ''' Give an item to a NPC. Availability of both is checked in
            processInput.py'''
        if item_obj == None:
            print('''What do you want to give to {0}?'''.format(self.name[0]))
        elif item_obj.__class__.__name__ in self.accept_items:
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


    def talk(self, objects):
        print('''"..."''')


    def x(self, objects):
        self.examine(objects)


class Drew(NPC):
    ''' Drew NPC '''
    def __init__(self):
        NPC.__init__(self)
        self.accept_items = ['Card'] # List of items the NPC can take
        self.description = 'Drew appears to have a deep affinity for t-shirts.'
        self.give_events = {
            'Card': self.get_card
        }
        self.name = ['Drew']
        self.talk_subjects = {
            'Card': self.talk_card
        }
        self.take_items = {
            'Card': self.take_card
        }
        self.visible = True


    def get_card(self, objects):
        ''' Actions to occur after giving Drew the card.'''
        print('''"Whoa, this card is sick brah! I can't just take it from you
            though, it's too expensive. I can appreciate you trying to figure
            out who it belongs to though. Let me see if I can help you out."''')


    def give(self, objects, item_obj=None):
        ''' Give an item to a NPC. Availability of both is checked in
            processInput.py'''
        if item_obj == None:
            print('''What do you want to give to {0}?'''.format(self.name[0]))
        elif item_obj.__class__.__name__ in self.accept_items:
            objects['Inventory']['Actor'].remove(item_obj)
            objects['Inventory'][self.__class__.__name__].append(item_obj)
            try:
                self.give_events[item_obj.__class__.__name__](objects)
            except KeyError:
                print('''You have given {0} the {1}.'''.format(
                self.name, item_obj.name))
        else:
            print('''"I don't have any need for that thing, 
                you can keep it."''')


    def hug(self, objects):
        print('''"Please stop squeezing me with your body."''')


    def kiss(self, objects):
        print('''"I'm just gonna pretend that didn't happen."''')


    def talk(self, objects, item_obj=None):
        if item_obj == None:
            print('''What do you want to talk to {0} about?'''.format(
                self.name[0]))
        else:
            try:
                self.talk_subjects[item_obj.__class__.__name__](objects)
            except KeyError:
                print('''"Sorry, I don't know much about the {0}."'''.format(
                    item_obj.name))


    def talk_card(self, objects):
        if objects['Items']['Card'] in objects['Inventory'][self.__class__.__name__]:
            print('''"Thanks for the card, I'll definitely use this"''')
        else:
            print('''"That's a sweet card! I'd love to take it off your hands if 
                you're not going to use it."''')


    def take(self, item_obj, objects):
        try:
            self.take_items[item_obj.__class__.__name__](objects)
        except KeyError:
            print('''{0} doesn't have the {1}.'''.format(
            self.name, item_obj.name))


    def take_card(self, objects):
        print('''TODO: Drew.take_card()''')

