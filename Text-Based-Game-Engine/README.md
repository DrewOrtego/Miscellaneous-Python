# Text-Based-Game-Engine

**Demonstrates**
* Object-oriented programming using Python 3 (recommended use in 3.4 or later)
* Organized and logical import commands with practical module design
* Logical use of "separation of concerns" principals
* Serializing Python objects to be saved to a text file and subsequently loaded back into the game
* Use of the pickle, textwrap, collections.ordereddict, glob, os, and operator.methodcaller modules

**Usage:**

    Run "main.py" in any interactive interpreter using Python 3.4 or later.
    
**Purpose:**

    This is the engine to a Zork-like text game, but written entirely in Python 3.
    I used this as a means to learn about object-oriented coding in Python, and
    this is the result. The "Demonstrates" section summarizes what I learned.
    
**Work Flow:**

    The game works with the following work flow in mind:
    1. Get valid input from the user.
    2. Implement changes to objects in the game, or print requested information.
    3. Repeat
     
    When you start a new game, all objects in the game-- items, rooms, the actor
    (which is essentially the player), and the new game are all created. Those 
    Python objects are then stored in a dict. This is the Object Map. The Object
    Map is accessed by various modules to alter all aspects of the game as you 
    play it. Say you want to "throw the book" at someone. When the game is given
    this command-- and verifies that it is a valid command given the current
    circumstances-- the book object is updated to reflect changes to it.
        
    This work flow is repeated until the actor dies or the game is completed.
    There's a lot more decision making that goes into this process, so check
    out the various folders in this repository to see how I've organized the 
    logic, and the purpose each set of modules serves.
    
**Input:**

    Refer to the help.py file in the userInterface folder for more information.
    If you're familiar with text-based games already, you should be comfortable
    with what you find here.
    
**Output:**

    You can create save files to save your game, otherwise all output is 
    printed to the console as you play the game.
