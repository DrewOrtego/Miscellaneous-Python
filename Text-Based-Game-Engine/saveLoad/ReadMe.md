# Miscellaneous-Python/Text-Based-Game-Engine/saveLoad

**Demonstrates**
* Use of the pickle module to serialize Python objects to a text file
* Provides an interface to save/load games which catches user error without crashing the game

**Purpose:**

   Allows the play to save their game to a text file so that it can be loaded
   later. This is only achievable when the modules are arranged so as to avoid
   circular imports, proper object permanence amid various state-changes,
   and proper design/logic when loading a new game to ensure that the load will
   achieve the as-you-left-it effect. All of this makes for a seemless experience
   when picking up a game from where the player left off.
