yodapy 2.0
======
(Now working in Python 2!)

**Description:**

    Prints random quotes from Star Wars characters from the original trilogy.



**Sample usage:**

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
