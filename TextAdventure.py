import random, os, sys
from time import sleep
from typewriter import typewriter

typewriter("Welcome to xxx!!!")
print()
typewriter("What do you wish to be called? ")
name = input()
typewriter("What race do you wanna be? Type \"raceinfo " "to find out details.")
print()
races = ["Dwarf", "Elf","Human", "Orc"]
typewriter("Do wish to be a dwarf, elf, human or an orc? ")
print()
race = input()
r = len(races)
for r in races:
    if race == "raceinfo":
        print(r, end='')
        sys.stdout.flush()
        sleep(0.5)
        print()

    #elif race == "Dwarf"

