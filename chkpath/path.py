"""
Copyright (c) 2018, Toby Slight. All rights reserved.
ISC License (ISCL) - see LICENSE file for details.
"""
import os


class Path:
    def __init__(self, path):
        self.path = path

    def exists(self):
        return os.path.exists(self.path)

    def isdir(self):
        return os.path.isdir(self.path)

    def isfile(self):
        return os.path.isfile(self.path)

    def chkdir(self):
        return self.exists() and self.isdir()

    def chkfile(self):
        return self.exists() and self.isfile()

    def mkdir(self):
        if self.chkdir():
            print("{} already exists.".format(self.path))
        else:
            os.mkdir(self.path)

    def mkfile(self):
        if self.chkfile():
            print("{} already exists.".format(self.path))
        else:
            open(self.path, 'a').close()
