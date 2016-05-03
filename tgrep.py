#!/usr/bin/env python

"""
Linewise recursive search for a pattern in text files ("tree grep").

(I wrote this before discovering `ack`. It's basically the same.)

Author: Joe Monaco
Created: 03-14-2007
Updated: 05-03-2016
"""

from __future__ import print_function

import os
import sys
import re

exclude_types = ['o','so','a','dylib','pdf','pyo','pyc','nib','plist',
    'rsrc','icns','gz','bz2','zip','tar','dmg','bundle','app']

exclude_dirs = ['bundle','app','pbxindex','pbxstrings','build','svn','git']

USAGE = "Usage: {} pattern [dir-or-file [...]]"


def blue(s):
    return '\033[0;36m' + s + '\033[0m'

def white(s):
    return '\033[0;37m' + s + '\033[0m'

def gray(s):
    return '\033[1;36m' + s + '\033[0m'

def highlight(s):
    return '\033[30;43m' + s + '\033[0m'


def tgrep_all(pattern, target_list):
    """
    Search all target arguments in target list for pattern.
    """
    for dir_or_file in target_list:
        if os.path.isdir(dir_or_file):
            tgrep(pattern, os.walk(dir_or_file))
        elif os.path.isfile(dir_or_file):
            head, tail = os.path.split(dir_or_file)
            targets = [(head, [], [tail])]
            tgrep(pattern, targets)
    return 0

def tgrep(pattern, targets):
    """
    Search target files for pattern and print colorized matches
    to the terminal.
    """
    for dirpath, dirnames, filenames in targets:
        for i, subd in enumerate(dirnames):
            if subd.split('.')[-1] in exclude_dirs:
                del dirnames[i]

        for fn in filenames:
            if fn.split('.')[-1] in exclude_types:
                continue

            lineno = 0
            printed_path = False
            pth = os.path.join(dirpath, fn)
            with open(pth, 'r') as f:
                for line in f:
                    lineno += 1
                    match = re.search(pattern, line, flags=re.I)
                    if match is None:
                        continue
                    if not printed_path:
                        print(blue(pth))
                        printed_path = True
                    start, end = match.span()
                    res = white('{:4d} '.format(lineno))
                    res += gray(line[:start])
                    res += highlight(line[start:end])
                    res += gray(line[end:].rstrip())
                    print(res)


if __name__ == "__main__":
    head, callname = os.path.split(sys.argv[0])
    if len(sys.argv) == 2:
        pattern = sys.argv[1]
        targets = [os.getcwd()]
    elif len(sys.argv) >= 3:
        if sys.argv[2] in ('-h', '--help'):
            print(USAGE.format(callname))
            sys.exit(1)
        pattern = sys.argv[1]
        targets = sys.argv[2:]
    else:
        print(USAGE.format(callname))
        sys.exit(1)

    sys.exit(tgrep_all(pattern, targets))
