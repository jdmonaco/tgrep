#!/usr/bin/env python
"""tree_search.py -- search a directory tree for text
   Usage: tree_search.py topdir searchterm

   Written by Joe Monaco, 3/14/2007
   Center for Theoretical Neuroscience
"""

import os
import sys
import re

exclude_types = ['o','so','a','dylib','pdf','pyo','pyc','nib','plist',
    'rsrc','icns','gz','bz2','zip','tar','dmg','bundle','app']
exclude_dirs = ['bundle','app','pbxindex','pbxstrings','build','svn','git']

def blue(s):
    return '\033[0;36m' + s + '\033[0m'

def gray(s):
    return '\033[0;37m' + s + '\033[0m'

def tree_search(text, topdir):
    "walk the tree, searching for text"
    td = os.path.realpath(topdir)
    if not os.path.exists(td):
        sys.stderr.write('Directory not found\n')
        return
    for d, dn, fn in os.walk(td):
        for i, subd in enumerate(dn):
            if subd.split('.')[-1] in exclude_dirs:
                del dn[i]
        for f in fn:
            if f.split('.')[-1] in exclude_types:
                continue
            f_lines = []
            try:
                fd = open(os.path.join(d, f), 'r')
            except IOError: continue
            else:
                f_lines = fd.readlines()
                fd.close()
            if len(f_lines) > 10000:
                continue
            l = 0
            once = False
            while f_lines:
                l += 1
                theline = f_lines.pop(0)
                if len(theline) > 255: continue
                if re.search(text, theline, flags=re.I):
                    if not once:
                        sys.stdout.write(blue(os.path.join(d, f)) + '\n')
                        once = True
                    sys.stdout.write(gray('%4d '%(l,)) + theline.strip() + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write(__doc__)
        sys.exit(1)
    tree_search(sys.argv[1], sys.argv[2])
