"""
Copyright (c) 2018, Toby Slight. All rights reserved.
ISC License (ISCL) - see LICENSE file for details.
"""
import os


def mkdir(path):
    if os.path.exists(path):
        print("{} already exists.".format(path))
    else:
        os.makedirs(path)


def mkfile(path):
    if os.path.exists(path):
        print("{} already exists.".format(path))
    else:
        open(path, 'a').close()
