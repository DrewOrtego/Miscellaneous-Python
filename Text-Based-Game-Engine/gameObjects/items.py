''' Items.py

    Holds all the in-game items and their methods.
    
    TODO: update Take function to be item-centric, and inherit functionality 
    instead of keeping item specific instructions in the Item parent class.
'''

import os
from gameObjects import events
from userInterface.formatOutput import formatOutput as print

class Item:
    def __init__(self):
        ''' The parent class for all item objects in the '''
        self.alias = '<Item ID>'
        self.adjective = []
        self.can_contain = False # Allows other items to be held within itself
        self.contains = [] # Lists items contained withint the container-item
        self.containable = False # Used in <take_from>; True if it can be stored
        self.contained = False # True if self is contained inside another item
        self.contains_item = False # True if the item contains another item
        self.description = "<Item Description>"
        self.display_name = None # Used for room descriptions and look command
        self.dropped = False # True implies the item was <taken> at one point
        self.first_examine = True # True means this item has not been examined
        self.has_item = False # True implies something is placed on the item
        self.is_available = False 
        self.is_open = False # not closed!
        self.is_taken = False # True if the item is in the actor's inventory
        self.name = ['<Item Name>', '<Item Name 2>']
        self.location = "" # Name of room or item where the item is intialized
        self.placed = False # Used to indicate an item rests upon another item
        self.size = None # 1 = pocketable, 2 = carryable, 3 = stationary
        self.takeable = False # Allows items to be added to actor's inventory
        self.visible = False # True alerts player to presence of Item using look


    def ask(self, objects, noun=None):
        print("The {0} doesn't seem to have much to say about that.".format(\
            self.name[0]))


    def ask_about(self, noun):
        self.ask(noun)


    def ask_for(self, noun):
        self.ask(noun)


    def close(self, objects):
        print("You cannot open the {}, let alone close it.".format(\
            self.name[0]))


    def destroy(self, objects):
        ''' Removes the object from the game entirely. Searches all 
            locations for the item.'''
        for item_list in objects['Inventory'].values():
            if self in item_list:
                item_list.remove(self)
                break


    def drop(self, objects):
        ''' Remove the object from the actor's inventory and place it in the
            current room's inventory.'''
        if self in objects['Inventory']['Actor']:
            objects['Inventory']['Actor'].remove(self)
            room_name = objects['CurrentRoom'].__class__.__name__
            objects['Inventory'][room_name].append(self)
            print("You have dropped the {}.".format(self.name[0]))
            self.is_taken = False
            self.dropped = True
        else:
            print("You are not carrying the {}.".format(self.name[0]))


    def eat(self, objects):
        print('''I don't think that the {} would agree with you.
            '''.format(self.name[0]))


    def enter(self, objects):
        print('''There is no enterance here.''')


    def examine(self, objects):
        self.first_examine = False
        print('''There doesn't seem to be anything particularly special
            about the {}.'''.format(self.name[0]))
        

    def exit(self, objects):
        print('''There is no exit here.''')
    

    def hit(self, objects):
        print('''Come on, don't be like that.''')
        

    def hug(self, objects):
        print('''You want to what?!''')
        

    def kiss(self, objects):
        print('''How's that {0} taste?'''.format(self.name[0]))
        

    def l(self, objects):
        self.look(objects)


    def look(self, objects):
        print(self.description)
        

    def move(self, objects):
        print("You cannot move the {}.".format(self.name[0]))


    def open(self, objects):
        print('''That doesn't look like something you can open.''')


    def place_in(self, objects, containing_item):
        self.place_inside(containing_item)


    def place_inside(self, containing_item, objects):
        ''' Place an item inside a containing_item. Updates the inventory for 
            the containing_item.'''
        if self.taken == False:
            print("You are not currently carrying the {0}".format(\
                self.name[0]))
        elif containing_item.can_contain == False:
            print("You cannot place items inside the {0}".format(\
                containing_item.name[0]))
        elif self.size > containing_item.size:
            print("The {0} is too large to fit inside the {1}.".format(\
                self.name[0], containing_item.name[0]))
        elif containing_item.is_open == False:
            print("The {} is currently closed.".format(\
                containing_item.name[0]))
        elif containing_item.contains_item:
            stored_item = obj.inventory_map.get(\
                containing_item.__class__.__name__)[0]
            print("The {0} already contains a {1}.".format(\
                containing_item.name[0], stored_item.name[0]))
        else:
            containing_item_name = containing_item.__class__.__name__
            objects['Inventory'][containing_item_name].append(self)
            objects['Inventory']['Actor'].remove(self)
            containing_item.contains_item = True
            self.contained = True
            print("The {0} is now in the {1}.".format(\
                self.name[0], containing_item.name[0]))
                

    def place_on(self, containing_item, objects):
        ''' Similar to the place_inside function. Updates the inventory of an 
            item to show that it is "holding" another item.'''
        if self.taken == False:
            message = "You are not currently carrying the {0}".format(self.name[0])
        elif containing_item.can_contain == False:
            message = "You cannot place items on the {0}".format(\
                containing_item.name[0])
        elif self.size > containing_item.size:
            message = "The {0} is too large to fit on the {1}.".format(\
                self.name[0], containing_item.name[0])
        elif containing_item.has_item == True:
            message = "The {0} already has the {1} on top of it.".format(\
                containing_item.name[0], self.name[0])
        else:
            containing_item_name = containing_item.__class__.__name__
            objects['Inventory'][containing_item_name].append(self)
            objects['Inventory']['Actor'].remove(self)
            containing_item.has_item = True
            self.placed = True
            message = "The {0} is now on top of the {1}.".format(\
                self.name[0], containing_item.name[0])
        print(message)


    def put_in(self, containing_item):
        self.place_inside(containing_item)


    def put_inside(self, containing_item):
        self.place_inside(containing_item)
        

    def put_on(self, containing_item):
        self.place_on(containing_item)


    def r(self):
        self.read()


    def read(self):
        print("You cannot read the {}.".format(self.name[0]))


    def remove(self, objects):
        if self.is_taken:    self.drop(objects)
        elif self.contained: self.take(objects)
        elif self.placed(objects):  self.take(objects)


    def remove_from(self, containing_item):
        self.take_from(containing_item)


    def take(self, objects):
        message = "You shouldn't see this message... item.py take function"
        if not self.takeable:
            message = "You cannot take the {}.".format(self.name[0])
        elif self in objects['Inventory']['Actor']:
            message = "You already have the {}.".format(self.name[0])
        elif self.contained or self.placed:
            # Remove the item from the ITEM that contains it, add to inventory
            room_name = objects['CurrentRoom'].__class__.__name__
            for i in objects['Inventory'][room_name]:
                if i.can_contain:
                    containing_item = i.__class__.__name__
                    if self in objects['Inventory'][containing_item]:
                        objects['Inventory'][containing_item].remove(self)
                        i.contains_item = False
                        objects['Inventory']['Actor'].append(self)
                        message = "You have taken the {}.".format(self.name[0])
                        break
            self.placed = False
            objects[containing_item].has_item = False
            self.is_taken = True
            self.taken()
        else:
            room_name = objects['CurrentRoom'].__class__.__name__
            objects['Inventory'][room_name].remove(self)
            objects['Inventory']['Actor'].append(self)
            message = "You have taken the {}.".format(self.name[0])
        print(message)


    def take_from(self, containing_item, objects):
        if not self.containable:
            print("The {0} might be a little too big to be placed in\
                another item.".format(self.name[0]))
        elif not containing_item.can_contain:
            print("The {0} does not allow anything to be stored in \
                it.".format(containing_item.name[0]))
        elif not containing_item.is_open:
            print("The {0} does not appear to be open.".format(\
                containing_item.name[0]))
        elif not containing_item.contains_item:
            print("The doesn't appear to be anything in the {0}."\
                .format(containing_item.name[0]))
        elif containing_item.contains_item:
            for i in objects['Inventory'][containing_item.__class__.__name__]:
                if i.name == self.name:
                    self.take()
                    break
                else:
                    print("The {0} is not inside the {1}".format(\
                        self.name[0], containing_item.name[0]))


    def taken(self, objects):
        ''' Performs an action upon taking an item. Does nothing by default.'''
        pass


    def throw(self, objects):
        current_room_obj = objects['Game'].current_room.__class__.__name__
        if self in objects['Inventory']['Actor']:
            print("You throw the {}.".format(self.name[0]))
            self.drop()
        elif self in obj.inventory_map[current_room_obj]:
            print("You do not have the {}.".format(self.name[0]))


    def use(self, objects):
        print('''How would you like to use the {}?'''.format(\
            self.name[0]))


    def x(self, objects):
        self.examine(objects)


# ------------------------------------------------------------------------------
# In-game items
# ------------------------------------------------------------------------------
class Booster(Item):
    def __init__(self):
        Item.__init__(self)
        self.adjective = ['magic', 'booster']
        self.can_contain = True
        self.display_name = ['"Magic: The Gathering" booster pack']
        self.description = "A pack of Magic cards from the Eternal Masters set."
        self.first_examine = True
        self.has_item = False
        self.name = ['pack']
        self.opened = False
        self.size = 1
        self.takeable = True
        self.visible = True


    def examine(self, objects):
        self.first_examine = False
        self.display_name = ['"Eternal Masters" booster pack'] + \
            self.display_name
        print('''It's a booster pack of Eternal Masters, hot off the presses!
            It is currently sealed. Who knows what cards could be found if it 
            were to be opened?!''')


    def open(self, objects):
        print('''Your hands tremble slightly and you clasp the pack in both 
            hands. You grab opposite ends of the pack and pull it apart to 
            separate the seal at the top, and slowly you open the pack.''', 
            await_input = "...Press any key to build suspense...")
        print('''The foil makes a distinct crinkling noise as you pull it apart,
            revealing the face of the first card in the pack. You hurriedly flip
            through the common cards to unmask some delightful uncommons, and 
            with bated breath you prepare to reveal the rare.''', 
            await_input = "...Press any key to intensify the suspense...")
        print('''You reveal the rare to be a... Winter Orb. I guess you can put
            that into an EDH deck if you want to alienate your play group. Oh 
            well.''', 
            await_input = "...Press any key to move on with your life.")
        print('''But wait, isn't there a foil in each pack of Eternal Masters? 
            You look behind the Winter Orb and see the edge of a blue, foil 
            card. Revealing it yields a Jace, The Mind Sculptor! You gasp as it 
            dawns on you that you can buy 3 or 4 regular Jace cards by selling 
            this one! However, this isn't yours, you found it here on the table,
            unguarded. Perhaps you should find the original owner?''',
            await_input = "...Press any key to test your morality.")
        print('''Will you choose to keep the card, or search for the true 
            owner?''')
        choice = input("keep or search? > ")
        while choice !=  'keep' and choice != 'search':
            os.system('cls')
            print('''You can keep the card, or search for the original 
                owner.''')
            choice = input("keep or search? > ")
        if choice == 'keep':
            message = '''You choose to keep the card for yourself. Just as you 
                begin to slip it into your pocket, a co-worker walks in and sees
                you. "JACE THIEF!!!", he shrieks. You try to explain the 
                situation, but it's too late: the Magic Judge's have arrived, 
                and faster than you can say "Tarmagoyf" you're taking a bean bag 
                shot to the gut. You spend the night in the Wizard's basement 
                dungeon, with no Jace. Tomorrow you will be permabanned from all
                tournaments and incessantly discussed on Reddit's MagicTCG 
                page.'''
            objects['Actor'].game_over(message)
        elif choice == 'search':
            print('''You decide to seek the try owner of the card and let him or
                her know of the bounty to be had! The card is now in your 
                inventory.''')
            objects['Inventory']['Actor'].append(objects['Items']['Card'])
            self.destroy(objects)
            self.opened = True


class Card(Item):
    def __init__(self):
        Item.__init__(self)
        self.adjective = ['magic']
        self.description = "It's a Magic card entitled 'Drew, The Job Seeker!'"
        self.display_name = ['card']
        self.first_examine = True
        self.name = ['card']
        self.size = 1
        self.takeable = True
        self.visible = True


    def eat(self, objects):
        print('''That would be the most expensive meal you've eaten in years! 
            You probably shouldn't do that.''')


    def examine(self, objects):
        self.first_examine = False
        self.name = ['magic card'] + self.name
        print('''It's a Magic: The Gathering card entitled "Jace, The Mind 
            Sculptor". It looks to be in mint condition. Judging from all the
            text on it, it's probably somewhat valuable.''')


    def read(self, objects):
        print('''+2: Look at the top card of target player's library. You may 
            put that card on the bottom of that player's library. 0: Draw three
            cards, then put two cards from your hand on top of your library in 
            any order. −1: Return target creature to its owner's hand. −12: 
            Exile all cards from target player's library, then that player 
            shuffles his or her hand into his or her library.''')


class DoorOne(Item):
    def __init__(self):
        Item.__init__(self)
        self.adjective = ['glass']
        self.description = "The glass door which leads to the hallway."
        self.display_name = ['door']
        self.first_examine = True
        self.has_item = False
        self.is_open = False
        self.name = ['door',]
        self.size = 3
        self.visible = False


    def examine(self, objects):
        self.first_examine = False
        self.display_name = ['glass door'] + self.display_name
        print('''An ordinary glass door, nothing special.''')


    def open(self, objects):
        ''' Allow door to open if the booster pack has been opened'''
        if self.is_open:
            print('''The door is already open.''')
        elif objects['Booster'].opened:
            self.is_open = True
            print('''You open the door.''')
        else:
            print('''Don't tempt yourself. You were told to stay put, 
                and you really shouldn't leave without a good reason.''')


    def close(self, objects):
        ''' Allow door to open if the booster pack has been opened'''
        if objects['Booster'].is_open == False:
            print('''The door is already closed, as it should be, unless you
                have something important to do.''')
        elif self.is_open == False:
            print('''The door is already closed.''')
        else:
            print('''You close the door.''')
            self.is_open = False


class DoorTwo(Item):
    def __init__(self):
        Item.__init__(self)
        self.adjective = []
        self.description = "A door which leads to the locked room."
        self.display_name = ['door']
        self.first_examine = True
        self.has_item = False
        self.is_open = False
        self.name = ['door',]
        self.size = 3
        self.visible = False


class Resume(Item):
    def __init__(self):
        Item.__init__(self)
        self.adjective = []
        self.can_contain = True
        self.description = "A very nice looking, well-formatted resume."
        self.display_name = ['resume']
        self.first_examine = True
        self.has_item = False
        self.name = ['resume',]
        self.size = 1
        self.takeable = True
        self.visible = True


    def read(self, objects):
        print('''The resume says...''')


    def examine(self, objects):
        self.first_examine = False
        print('''This looks to be the resume of one "Andrew Ortego". Just look
            at all that experience!''')


class Table(Item):
    def __init__(self):
        Item.__init__(self)
        self.adjective = ['large', 'ikea']
        self.can_contain = False
        self.description = "A large table used for meetings."
        self.display_name = ['large table']
        self.first_examine = True
        self.has_item = False
        self.name = ['table']
        self.size = 3
        self.takeable = False
        self.visible = False


    def examine(self, objects):
        self.first_examine = False
        self.display_name = ['large Ikea table'] + self.name
        print('''It's from Ikea! No expense was spared!''')

