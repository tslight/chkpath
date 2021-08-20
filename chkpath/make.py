"""
Copyright (c) 2018, Toby Slight. All rights reserved.
ISC License (ISCL) - see LICENSE file for details.
"""
import os


def mkdir(path):
    """
    Make nested directories if they don't exist. Pretty redundant since
    os.makedirs does this anyway, but I've come this far, so..

    Quite nice to have as a command line util though... except mkdir -p
    exists... Goddamnit!
    """
    if os.path.exists(path):
        print("{} already exists.".format(path))
    else:
        try:
            os.makedirs(path, exist_ok=True)
        except OSError:
            print("Uh oh - something went awry!")
        else:
            print("Successfully created {}".format(path))


def mkfile(path):
    """
    Makes files in nested directories. I think this one is actually mildly
    useful cos it creates the parent directory if that doesn't exist.
    """
    if os.path.exists(path):
        print("{} already exists.".format(path))
    else:
        try:
            parent = os.path.abspath(os.path.join(path, os.pardir))
            os.makedirs(parent, exist_ok=True)
            open(path, 'a').close()
        except OSError:
            print("Uh oh - something went awry!")
        else:
            print("Successfully created {}".format(path))
