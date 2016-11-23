import sys
from time import sleep


def typewriter(text, sleeptime = 0.2):
    for char in text:
        sleep(sleeptime)
        sys.stdout.write(char)
        sys.stdout.flush()