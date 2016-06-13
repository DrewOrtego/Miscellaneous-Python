# Miscellaneous-Python/Text-Based-Game-Engine/commandProcessing

**Demonstrates**
* Use of pickle to save and load game objects to and from a file
* Straight forward implementation of all valid in-game commands
* Logical manner of tokenizing and validating user-input
    
    
**Purpose:**

      Contains the modules used to process the user's commands. This is made easy
      buy storing a master file of all valid commands (commands.py) and using
      a tokenizing mechanism (tokenizer.py) to search for valid command patterns.
      main.py utilizes the modules here to determine if the user has entered a
      valid command, if it has use in the way the user entered it, and finally
      whether or not the command can be executed given the player's current
      circumstances in the game.
