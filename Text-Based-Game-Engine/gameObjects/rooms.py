''' Rooms.py

    Holds all in-game rooms and their methods. A room can be thought of as any 
    place the game allows the player to make choices and interact with the game,
    items in the room or inventory, enter commands such as "help", etc. A room 
    is basically each state in a state-based system.
'''

from gameObjects import events
from userInterface.formatOutput import formatOutput as print


class Room:
    def __init__(self):
        self.name = "<Room Name>"
        self._description = "<Decorator Room Description>"
        self.default_direction = "You can't go that way."
        self.first_visit = None


    def   up(self, objects) : return {'message' : self.default_direction}
    def down(self, objects) : return {'message' : self.default_direction}
    def north(self, objects): return {'message' : self.default_direction}
    def  east(self, objects): return {'message' : self.default_direction}
    def south(self, objects): return {'message' : self.default_direction}
    def  west(self, objects): return {'message' : self.default_direction}
    def northeast(self, objects): return {'message' : self.default_direction}
    def southeast(self, objects): return {'message' : self.default_direction}
    def southwest(self, objects): return {'message' : self.default_direction}
    def northwest(self, objects): return {'message' : self.default_direction}
    def  u(self, objects): return self.up(objects)
    def  d(self, objects): return self.down(objects)
    def  n(self, objects): return self.north(objects)
    def  e(self, objects): return self.east(objects)
    def  s(self, objects): return self.south(objects)
    def  w(self, objects): return self.west(objects)
    def ne(self, objects): return self.northeast(objects)
    def se(self, objects): return self.southeast(objects)
    def sw(self, objects): return self.southwest(objects)
    def nw(self, objects): return self.northwest(objects)


    def look(self, objects):
        ''' Prints the current room's description, and any available items.'''
        msg = objects['CurrentRoom'].description
        current_room = objects['CurrentRoom'].__class__.__name__
        visible_items = [i for i in objects['Inventory'][current_room] 
            if type(i).__name__ in objects['Items'] and i.visible]
        for i in visible_items:

            # For 1 item
            if i.visible and len(visible_items) == 1:
                msg += (' There is a {} here.'.format(i.name[0]))

            # For 2 items
            elif i.visible and len(visible_items) == 2:
                if visible_items.index(i) == 0:
                    msg += (' There is a {} '.format(i.name[0]))
                else: 
                    msg += (' and a {} here.'.format(i.name[0]))

            # For more than 2 items
            elif i.visible and len(visible_items) > 1:
                if visible_items.index(i) == 0:
                    msg += ('There is a {}, '.format(i.name[0]))
                elif visible_items.index(i) != len(visible_items) - 1:
                    msg += (' a {}, '.format(i.name[0]))
                else:
                    msg += (' and a {} here.'.format(i.name[0]))

            # For any item(s) found within another item             
            if i.contains_item:
                stored_item = visible_items
                if stored_item.visible:
                    msg += (' There is a {0} contained in the {1}.'.format(\
                        stored_item.name[0],
                        i.name[0]))

        ## For any NPC(s) found in the room.
        visible_npcs = [n for n in objects['Inventory'][current_room]
            if type(n).__name__ in objects['Npcs'] and n.visible]
        for n in visible_npcs:

            # For 1 npc
            if n.visible and len(visible_npcs) == 1:
                msg += (' {} is here.'.format(n.name[0]))

            # For 2 npc's
            elif n.visible and len(visible_npcs) == 2:
                if visible_npcs.index(n) == 0:
                    msg += ('{} and '.format(n.name[0]))
                else: 
                    msg += (' {} are here.'.format(n.name[0]))

            # For more than 2 npc's
            elif n.visible and len(visible_npcs) > 1:
                if visible_npcs.index(n) == 0:
                    msg += ('{}, '.format(n.name[0]))
                elif visible_npcs.index(i) != len(visible_npcs) - 1:
                    msg += ('{}, '.format(n.name[0]))
                else:
                    msg += (' and {} are here.'.format(n.name[0]))
        print(msg)
        
    
class InterviewRoom(Room):
    def __init__(self):
        Room.__init__(self)
        self.description = '''You are in a meeting room which has a table in the 
            center of it and six chairs all around. It's quite bland in here. There
            is a door to the north which leads to the hallway.'''
        self.name = 'Interview Room'


    def north(self, objects):
        if objects['Items']['Booster'].opened:
            objects['Items']['DoorOne'].is_open = True
            return {'movement' : objects['Rooms']['Hallway']}
        else:
            return {'message': '''You were told to stay put, and you really
                shouldn't leave without a good reason.'''}


    def look(self, objects):
        ''' Prints the current room's description, and any available items.'''
        msg = objects['CurrentRoom'].description
        current_room = objects['CurrentRoom'].__class__.__name__
        visible_items = [i for i in objects['Inventory'][current_room] 
            if type(i).__name__ in objects['Items'] and i.visible]

        for i in visible_items:
            # For 1 item
            if i.visible and len(visible_items) == 1:
                msg += (' There is a {0} on the {1}.'.format(i.display_name[0], 
                    objects['Items']['Table'].display_name[0]))

            # For 2 items
            elif i.visible and len(visible_items) == 2:
                if visible_items.index(i) == 0:
                    msg += (' There is a {} '.format(i.display_name[0]))
                else: 
                    msg += (' and a {0} on the {1}.'.format(i.display_name[0], 
                        objects['Items']['Table'].display_name[0]))

            # For more than 2 items
            elif i.visible and len(visible_items) > 1:
                if visible_items.index(i) == 0:
                    msg += ('There is a {}, '.format(i.display_name[0]))
                elif visible_items.index(i) != visible_items - 1:
                    msg += (' a {}, '.format(i.display_name[0]))
                else:
                    msg += (' and a {0} on the {1}.'.format(i.display_name[0], 
                        objects['Items']['Table'].display_name[0]))

            if i.contains_item:
                stored_item = objects['Inventory'][current_room]
                if stored_item.visible:
                    msg += (' There is a {} inside the {}.'.format(\
                        stored_item.name[0],
                        i.name[0]))

        ## For any NPC(s) found in the room.
        visible_npcs = [n for n in objects['Inventory'][current_room]
            if type(n).__name__ in objects['Npcs'] and n.visible]
        for n in visible_npcs:

            # For 1 npc
            if n.visible and len(visible_npcs) == 1:
                msg += (' {} is here.'.format(n.name[0]))

            # For 2 npc's
            elif n.visible and len(visible_npcs) == 2:
                if visible_npcs.index(n) == 0:
                    msg += ('{} and '.format(n.name[0]))
                else: 
                    msg += (' {} are here.'.format(n.name[0]))

            # For more than 2 npc's
            elif n.visible and len(visible_npcs) > 1:
                if visible_npcs.index(n) == 0:
                    msg += ('{}, '.format(n.name[0]))
                elif visible_npcs.index(i) != len(visible_npcs) - 1:
                    msg += ('{}, '.format(n.name[0]))
                else:
                    msg += (' and {} are here.'.format(n.name[0]))
        print(msg)


class Hallway(Room):
    def __init__(self):
        Room.__init__(self)
        self.description = '''The hallway which connects the meeting room to the 
        south, a room to the north, and the offices to the east and west.'''
        self.name = 'Hallway'


    def north(self, objects):
        if events.meet_drew == True:
            return {'movement' : objects['Rooms']['LockedRoom']}
        else:
            return {'message': '''The door to this room is locked.'''}


    def east(self, objects):
        return {'message': '''This area leads to more offices and meeting rooms,
            where some very important stuff is happening. You probably shouldn't
            be wandering around there.'''}


    def south(self, objects):
        objects['DoorOne'].is_open = True
        return {'movement': objects['Rooms']['InterviewRoom']}


    def west(self, objects):
        return {'movement': objects['Rooms']['OfficeSpaceNorth']}


class LockedRoom(Room):
    def __init__(self):
        Room.__init__(self)
        self.description = 'Locked Room.'
        self.name = 'Locked Room'


    def south(self, objects):
        return {'movement' : objects['Rooms']['Hallway']}


class OfficeSpaceNorth(Room):
    def __init__(self):
        Room.__init__(self)
        self.description = 'North portion of the office floor.'
        self.name = 'Office Floor (North)'


    def east(self, objects):
        return {'movement': objects['Rooms']['Hallway']}


    def south(self, objects):
        return {'movement': objects['Rooms']['OfficeSpaceSouth']}


class OfficeSpaceSouth(Room):
    def __init__(self):
        Room.__init__(self)
        self.description = 'South portion of the office floor.'
        self.name = 'Office Floor (South)'


    def east(self, objects):
        return {'movement': objects['Rooms']['Hallway']}


    def north(self, objects):
        return {'movement': objects['Rooms']['OfficeSpaceSouth']}

