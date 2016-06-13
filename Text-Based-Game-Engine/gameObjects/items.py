''' Items.py

    Holds all the in-game items and their methods.
    
    TODO: update Take function to be item-centric, and inherit functionality 
    instead of keeping item specific instructions in the Item parent class.
'''

from gameObjects import events
from userInterface.formatOutput import formatOutput as print

class Item:
    def __init__(self):
        ''' The parent class for all item objects in the '''
        self.alias = '<Item ID>'
        self.adjective = []
        self.can_contain = False # Allows other items to be held within itself.
        self.contains = [] # Lists items contained withint the container-item
        self.containable = False # Used in <take_from>; True if it can be stored
        self.contained = False # True if self is contained inside another item.
        self.contains_item = False # True if the item contains another item.
        self.description = "<Item Description>"
        self.dropped = False # True implies the item was <taken> at one point.
        self.has_item = False # True implies something is placed on the item.
        self.is_available = False
        self.is_open = False # not closed!
        self.is_taken = False # True if the item is in the actor's inventory.
        self.name = ("<Item Name>", "<Item Name 2>")
        self.location = "" # Name of room or item where the item stored.
        self.placed = False # Used to indicate an item rests upon another item.
        self.size = None # 1 = small, 2 = medium, 3 = venti.
        self.takeable = False # Allows items to be added to actor's inventory.
        self.visible = False # True if the item is printed by the <look> command


    def ask(self, objects, noun=None):
        print("The {0} doesn't seem to have much to say.".format(\
            self.name[0]))
        

    def ask_about(self, noun):
        self.ask(noun)
        

    def ask_for(self, noun):
        self.ask(noun)


    def close(self, objects):
        print("You cannot open the {}, let alone close it.".format(\
            self.name[0]))


    def drop(self, objects):
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
        print('''There doesn't seem to be anything particularly special
            about the {}.'''.format(self.name[0]))
        

    def exit(self, objects):
        print('''There is no exit here.''')
        

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
        ''' self is the item being placed inside the containing_item.'''
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

            if self.name[0] == 'pawn' and containing_item.name[0] == 'board':
                message += " A door to the east suddenly appears!"
                events.pawn_on_board = True
                objects['SecondRoom'].description += \
                    ' A secret door has opened to the east.'
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
            # Remove the item from the ITEM that contains it, add to inventory.
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
            
        # Code to execute if the pawn is taken from the board (activates a room)
        if objects['ChessPiece'] in objects['Inventory']['Actor']:
            if events.pawn_on_board:
                events.pawn_on_board = False
                message += " The secret door slides shut."
                objects['SecondRoom'].description = '''This room is completely 
                    black, and the only source of light comes from the white 
                    room to the south illuminating a chess board towards the 
                    back of the room.'''
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
class Cake(Item):
    def __init__(self):
        Item.__init__(self)
        self.description = "A delicious-looking cake!"
        self.name = ('cake',)
        

    def cut(self, objects):
        print('''You have nothing that can cut the cake.''')
        

    def eat(self, objects):
        print('''You enjoy the spoils of puzzle-solving by indulging in
            a slice of the cake.''')
        objects['Game'].win()
        

    def slice(self, objects):
        print('''You have nothing with which you can slice the cake.''')
        
        
class ChessBoard(Item):
    def __init__(self):
        Item.__init__(self)
        self.can_contain = True
        self.description = "A marble chess board."
        self.first_examine = True
        self.has_item = False
        self.name = ('board',)
        self.location = "SecondRoom"
        self.size = 2
        

    def examine(self, objects):
        message = self.description
        if events.pawn_on_board:
            message += ' All the pieces of the chess board are now in place.'
        else:
            message += ' It is set up for a game, but a single pawn is missing.'
        print(message)
        
        
class ChessPiece(Item):
    def __init__(self):
        Item.__init__(self)
        self.adjective = ['small',]
        self.alias = 'piece'
        self.containable = True
        self.contained_in = ""
        self.description = "A small, black, marble pawn from a chess set."
        self.first_take = True
        self.name = ('pawn',)
        self.location = "SecondRoom"
        self.size = 1
        self.takeable = True
        self.visible = True
        

    def examine(self, objects):
        print('''It's one of the black pawns from a chess board.''')

