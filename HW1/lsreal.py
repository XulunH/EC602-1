#!/usr/bin/env python3
import sys
from lsone import lsone
from lslong import lslong
from lsfiles import lsfiles
from lscol import lscol

def lsreal():
    args = sys.argv[1:]

    if "-l" in args:
        lslong()
    elif "-C" in args:
        lscol()
    elif "-1" in args:
        lsone()
    else:
        lsfiles()
        

if __name__ == "__main__":
    lsreal()
