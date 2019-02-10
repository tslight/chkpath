"""
Copyright (c) 2018, Toby Slight. All rights reserved.
ISC License (ISCL) - see LICENSE file for details.
"""
import argparse
import os
from .path import Path


def getargs():
    parser = argparse.ArgumentParser(
        description='Check existence of paths and optionally create them.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', '--directory', action="store_true",
                       help="Look for (and optionally create) directory.")
    group.add_argument('-f', '--file', action="store_true",
                       help="Look of (and optionally create) files.")
    parser.add_argument('-c', '--create', action="store_true",
                        help="Create the file system node.")
    parser.add_argument("path", nargs='?', default=".", help="a path to check")
    return parser.parse_args()


def main():
    args = getargs()
    path = os.path.abspath(args.path)
    path = Path(path)
    if args.directory:
        if args.create:
            path.mkdir()
        else:
            path.chkdir()
    elif args.file:
        if args.create:
            path.mkfile()
        else:
            path.chkfile()


if __name__ == '__main__':
    main()
