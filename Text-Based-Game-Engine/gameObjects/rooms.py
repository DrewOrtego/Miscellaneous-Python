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
        
        
    @property
    def description(self):
        return self._description
                     

    def   up(self, objects)  : return {'message' : self.default_direction}
    def down(self, objects)  : return {'message' : self.default_direction}
    def north(self, objects) : return {'message' : self.default_direction}
    def  east(self, objects) : return {'message' : self.default_direction}
    def south(self, objects) : return {'message' : self.default_direction}
    def  west(self, objects) : return {'message' : self.default_direction}
    def northeast(self, objects) : return {'message' : self.default_direction}
    def southeast(self, objects) : return {'message' : self.default_direction}
    def southwest(self, objects) : return {'message' : self.default_direction}
    def northwest(self, objects) : return {'message' : self.default_direction}
    
    def  u(self, objects) : return self.up(objects)
    def  d(self, objects) : return self.down(objects)
    def  n(self, objects) : return self.north(objects)
    def  e(self, objects) : return self.east(objects)
    def  s(self, objects) : return self.south(objects)
    def  w(self, objects) : return self.west(objects)
    def ne(self, objects) : return self.northeast(objects)
    def se(self, objects) : return self.southeast(objects)
    def sw(self, objects) : return self.southwest(objects)
    def nw(self, objects) : return self.northwest(objects)
    
    
class FirstRoom(Room):
    def __init__(self):
        Room.__init__(self)
        self.first_visit  = True
        self.default_direction = 'You cannot go that way from here.'
        self.description = '''You are in a well-lit, completely white room. The
            walls are glossy, and it's hard to differentiate the dimensions of
            this room. There is a black passageway to the north.'''
        self.name = 'White Room'

    @property
    def description(self):
        return self._description
        

    @description.setter
    def description(self, description):
        self._description = description
            

    def east(self, objects):
        if objects['ChessPiece'] in objects['Inventory']['ChessBoard']:
            return {'movement' : objects['ThirdRoom']}
        else:
            return {'message' : self.default_direction}
        

    def north(self, objects):
        if objects['Game'].tutorial_mode and self.first_visit == True:
            objects['FirstRoom'].first_visit = False
        return {'movement' : objects['SecondRoom']}
        
        
class SecondRoom(Room):
    def __init__(self):
        Room.__init__(self)
        self.default_direction = 'You cannot go that way.'
        self.description = '''This room is completely black, and the only source
            of light comes from the white room to the south illuminating a chess
            board towards the back of the room.'''
        self.first_visit = True
        self.name = 'Black Room'
        
    @property
    def description(self):
        return self._description
    

    @description.setter
    def description(self, new_desc):
        self._description = new_desc
        

    def east(self, objects):
        if events.pawn_on_board:
            return {'movement' : objects['ThirdRoom']}
        else:
            return {'message' : self.default_direction}
        

    def south(self, objects):
        return {'movement' : objects['FirstRoom']}
        
        
class ThirdRoom(Room):
    def __init__(self):
        Room.__init__(self)
        self.default_direction = 'You cannot go that way.'
        self.description = '''The final room! There's a cake for you here so
            that you can celebrate beating the demo.'''
        self.name = 'Gray Room'
        
    @property
    def description(self):
        return self._description
    

    @description.setter
    def description(self, new_desc):
        self._description = new_desc
        
        
    def west(self, objects):
        return {'movement' : objects['SecondRoom']}

