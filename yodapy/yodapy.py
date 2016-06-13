"""
yodapy.py
Andrew Ortego
ortegoa@gmail.com

Description:
Prints random quotes from Star Wars characters from the original trilogy.

Sample usage:
>>> import yodapy
>>> Yoda = yodapy.quotes()
>>> Yoda.speak()

...prints a random quote from Master Yoda...

>>> Han = yodapy.quotes("HAN")
>>> Han.speak()

...prints a random quote from Han Solo...

>>> Drew = yodapy.quotes("DREW")
>>> Drew.speak()

...prints an error message since there is no character 'Drew'...

"""
__version__ = '2.0'

import os, re, string
from os.path import abspath
from random import randint

script_files = ['anh.txt', 'tesb.txt', 'rotj.txt']
scripts = [ os.path.join(abspath(os.path.dirname(__file__)), s)
            for s in script_files
          ]

class quotes:
    """
    Complete list of each character whose quote(s) you can print.
        ACKBAR
        AIDE
        ANAKIN
        ANNOUNCER
        ANOTHER PART OF THE FOREST
        ASSISTANT OFFICER
        AUNT BERU
        BARTENDER
        BASE VOICE
        BEN
        BERU
        BIB
        BIGGS
        BOBA FETT
        BOUSHH
        BOUSSH
        BUNKER COMMANDER
        CAMIE
        CAPTAIN
        CHIEF PILOT
        CHIEF
        COMMANDER
        COMMUNICATIONS OFFICER
        CONTROL OFFICER
        CONTROL ROOM COMMANDER
        CONTROLLER
        CREATURE
        DACK
        DEAK
        DEATH STAR CONTROLLER
        DEATH STAR INTERCOM VOICE
        DECK OFFICER
        DERLIN
        DISSOLVE TO
        DODONNA
        EMPEROR
        EXPANDED SCREENPLAY
        EXTERIOR
        FIRST CONTROLLER
        FIRST OFFICER
        FIRST TROOPER
        FIXER
        GANTRY OFFICER
        GENERAL MADINE
        GOLD FIVE
        GOLD LEADER
        GOLD TWO
        GRAY LEADER
        GREEDO
        GREEN LEADER
        GUARD
        HAN
        HEAD CONTROLLER
        HOBBIE
        HUMAN
        IMPERIAL OFFICER
        IMPERIAL SOLDIER
        INTERCOM VOICE
        INTERIOR
        JABBA
        JANSON
        JERJERROD
        JOH YOWZA
        LANDO
        LEIA
        LIEUTENANT
        LUKE
        MADINE
        MASSASSI INTERCOM VOICE
        MEDICAL DROID
        MON MOTHMA
        MOTTI
        NAVIGATOR
        NEEDA
        NIEN
        NINEDENINE
        OFFICER CASS
        OFFICER
        OOLA
        OPERATOR
        OWEN
        OZZEL
        PIETT
        PILOT
        PILOTS
        PORKINS
        READ LEADER
        REBEL CAPTAIN
        REBEL FIGHTER
        REBEL OFFICER
        REBEL PILOT
        RED ELEVEN
        RED LEADER
        RED NINE
        RED SEVEN
        RED TEN
        RED THREE
        RED TWO
        RIEEKAN
        SCOUT
        SECOND COMMANDER
        SECOND CONTROLLER
        SECOND OFFICER
        SECOND THREEPIO
        SECOND TROOPER
        SENIOR CONTROLLER
        SHUTTLE CAPTAIN
        STORMTROOPER
        STRANGE VOICE
        TAGGE
        TARKIN
        TECHNICIAN
        THREEPIO
        TITLE CARD
        TRACKING OFFICER
        TRENCH OFFICER
        TROOPER VOICE
        TROOPER
        VADER
        VEERS
        VOICE OVER DEATH STAR INTERCOM
        VOICE
        WEDGE
        WILLARD
        WINGMAN
        WIPE TO
        WOMAN CONTROLLER
        WOMAN
        YODA
        ZEV
    """
    def __init__(self, character="YODA"):
        self.character = character.upper()
        self.quote_list = []

        capture = False
        current_quote = ""
        name_pattern = "^[A-Z]*:"
        name = re.compile(name_pattern)

        for file_name in scripts:
            with open(file_name) as script:
                for line in iter(script): # Reads the script one line at a time
                    if name.match(line) and capture == True:
                        capture = False
                        self.quote_list.append(current_quote)
                        current_quote = ""
                    elif self.character + ":" in line:
                        capture = True
                        current_quote += line
                    elif capture == True:
                        current_quote += line


        if self.quote_list == []:
            self.quote_list = ["NO MATCH FOUND: Choose a known character you must."]


    def speak(self):
        """ Prints a random quote from the quote object."""
        print(self.quote_list[randint(0, len(self.quote_list)-1)])

