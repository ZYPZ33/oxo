#!/usr/bin/env python3
from sys import argv
from os import system

filename="oxo.py"
directory="/usr/local/bin"

def runGame():
    with open(filename) as code:
        exec(code.read())

if len(argv) > 1:
    if "install" in argv:
        system("install",filename,directory)
    if "run" in argv:
        runGame()
else:
    runGame()
