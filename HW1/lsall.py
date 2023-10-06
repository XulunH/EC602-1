#!/usr/bin/env python3
import sys
from lsone import lsone
from lslong import lslong
from lsfiles import lsfiles
from lscol import lscol
from lsreal import lsreal


def lsall():
    # The name under which the script was invoked
    invoked_as = sys.argv[0].split('/')[-1]

    if invoked_as == 'lsone':
        lsone()
    elif invoked_as == 'lscol':
        lscol()
    elif invoked_as == 'lslong':
        lslong()
    elif invoked_as == 'lsfiles':
        lsfiles()
    elif invoked_as == 'lsreal':
        lsreal()
    else:
        print("Command not recognized")

if __name__ == '__main__':
    lsall()

