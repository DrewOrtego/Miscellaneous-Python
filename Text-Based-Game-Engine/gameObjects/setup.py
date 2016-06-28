''' setup.py

    Imports all objects and maps them to a dictionary. The dict is used to keep
    track of all instantiated objects used in the game and is updated as the
    game is played.
'''


from gameObjects import actor, game, items, rooms

# Initialize all objects at the start of the game
current_game  = game.Game()
current_actor = actor.Actor()

# rooms ----------------------------------
first_room  = rooms.FirstRoom()
second_room = rooms.SecondRoom()
third_room = rooms.ThirdRoom()

# items ----------------------------------
cake = items.Cake()
chess_board = items.ChessBoard()
chess_piece = items.ChessPiece()

# Store references to the objects that are used throughout the game
objects = {
    # Used to save data
    'CurrentRoom': first_room,
    'Game': current_game,
    'Actor': current_actor,
    'FirstRoom': first_room,
    'SecondRoom': second_room,
    'ThirdRoom': third_room,
    'Cake': cake,
    'ChessBoard': chess_board,
    'ChessPiece': chess_piece,
    
    'Inventory': {
        'Actor': [],
        # Rooms --------------------------------------
        'FirstRoom': [],
        'SecondRoom': [chess_board, chess_piece,],
        'ThirdRoom': [cake,],
        # Items --------------------------------------
        'ChessBoard': [],
    }
}