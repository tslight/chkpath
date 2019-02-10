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
        if self.exists():
            if not self.isdir():
                return "{} is not a directory.".format(self.path)
        else:
            return "{} doesn't exist.".format(self.path)

    def chkfile(self):
        if self.exists():
            if not self.isfile():
                return "{} is not a file.".format(self.path)
        else:
            return "{} doesn't exist.".format(self.path)

    def mkdir(self):
        if self.exists():
            print("{} already exists.".format(self.path))
        else:
            os.mkdir(self.path)

    def mkfile(self):
        if self.exists():
            print("{} already exists.".format(self.path))
        else:
            open(self.path, 'a').close()
