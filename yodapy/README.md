# Repo-Name

**Demonstrates**
* Use of Regular Expressions to parse text files
* Intimate knowledge of the Star Wars universe and various quotes
* Does not include dialog from the prequels because they're terrible

**Description:**

    Prints random quotes from Star Wars characters from the original trilogy.

**Sample Usag:**

     >>> import yodapy
     >>> Yoda = yodapy.quotes()
     >>> Yoda.speak()
     
     YODA: No! Try not. Do. Or do not. There is no try.
     
     >>> Han = yodapy.quotes("HAN")
     >>> Han.speak()
     
     HAN: We're losing our deflector shield. Go strap yourself in, I'm
     going to make the jump to light speed.
     
     >>> Drew = yodapy.quotes("DREW")
     >>> Drew.speak()
     
     NO MATCH FOUND: Choose a known character you must.
