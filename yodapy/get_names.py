"""
yodapy.py
Andrew Ortego
ortegoa@gmail.com

Description:
Sorts and prints all valid character names for use in yodapy.py.
"""

import os, re, string
from os.path import abspath
from random  import randint

script_files = ['anh.txt', 'tesb.txt', 'rotj.txt']
scripts      = [ os.path.join(abspath(os.path.dirname(__file__)), s)
                 for s in script_files]

pattern = "^[A-Z\s]*:"
p = re.compile(pattern)
characters = []

for file_name in scripts:
    with open(file_name) as script:
        for lines in script.readlines():
            if p.findall(lines):
                result = p.match(lines)
                characters.append(result.group(0))
for x in sorted(set(characters)):
    print x[:-1]