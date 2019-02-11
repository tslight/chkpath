"""
Copyright (c) 2018, Toby Slight. All rights reserved.
ISC License (ISCL) - see LICENSE file for details.
"""
import argparse
import os
from .make import mkdir, mkfile


def getargs():
    parser = argparse.ArgumentParser(
        description='Create a path if it doesn\'t already exist.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', '--directory', action="store_true",
                       help="Look for and create directory.")
    group.add_argument('-f', '--file', action="store_true",
                       help="Look for and create file.")
    parser.add_argument("path", nargs='?', default=".", help="a path to check")
    return parser.parse_args()


def main():
    args = getargs()
    path = os.path.abspath(args.path)
    if args.directory:
        mkdir(path)
    elif args.file:
        mkfile(path)


if __name__ == '__main__':
    main()
