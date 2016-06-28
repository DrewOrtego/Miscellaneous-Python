''' setup.py

    Imports all objects and maps them to a dictionary. The dict is used to keep
    track of all instantiated objects used in the game and is updated as the
    game is played.
'''

from gameObjects import actor, game, items, rooms, npcs

# Initialize all objects at the start of the game
current_game  = game.Game()
current_actor = actor.Actor()

# rooms ----------------------------------
interview_room  = rooms.InterviewRoom()
hallway         = rooms.Hallway()
office_space_n  = rooms.OfficeSpaceNorth()
office_space_s  = rooms.OfficeSpaceSouth()
locked_room     = rooms.LockedRoom()

# items ----------------------------------
card    = items.Card()
door1   = items.DoorOne()
door2   = items.DoorTwo()
resume  = items.Resume()
booster = items.Booster()
table   = items.Table()

# npcs -----------------------------------
drew = npcs.Drew()

# Store references to the objects that are used throughout the game
objects = {
    'CurrentRoom': interview_room,
    'Game': current_game,
    'Actor': current_actor,
    'Rooms': {
        'InterviewRoom': interview_room,
        'Hallway': hallway,
        'LockedRoom': locked_room,
        'OfficeSpaceNorth': office_space_n,
        'OfficeSpaceSouth': office_space_s,
    },
    'Items': {
        'Card': card,
        'Resume': resume,
        'Booster': booster,
        'Table': table,
        'DoorOne': door1,
        'DoorTwo': door2,
    },
    'Npcs': {
        'Drew': drew,
    },
    'Inventory': {
        'Actor': [],
        'InterviewRoom': [booster, resume, table, door1],
        'Hallway': [door1, door2],
        'OfficeSpaceNorth': [],
        'OfficeSpaceSouth': [drew],
        'LockedRoom': [door2],
        'Drew': [],
    },
}