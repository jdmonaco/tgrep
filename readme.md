# tgrep

Recursively search entire directories of text files for a pattern match. Get nicely colorized and line-numbered output in your terminal.

I originally wrote this before I knew about `ack` ([beyondgrep.com](http://beyondgrep.com)). But, `tgrep` is like a really simplified `ack` in a little python script. It is probably worse in a number of ways and edge cases, because `ack` has a "website" and a "community", and this is just a little script I wrote to help me search directories of source files. But I don't really know. Improvements over `ack` (that I can see!) include that the line numbers are right justified in a 4-char column and are white instead of dark gray, which makes the search result line indentation more consistent and the line numbers easier to read. Also, it's a short and simple script, so it's easy to understand what it's doing and to change it for your own use case.

It chooses files to search by excluding certain extensions (e.g., `*.pdf`, `*.out`) and directories (e.g., those ending in `app` or `git` after a `.`). The exclusions are defined at the top of the script. I wrote those exclusion lists like 8 years ago, so they should probably be improved.

It's pretty easy to use:

    Usage: tgrep.py pattern [dir-or-file [...]]

It will search the current directory if you don't pass in any targets.

## Why "t"?

I called it `tgrep` because `tree grep` is how I think of it.

## Installation

Download the script somewhere and make a symbolic link to it from a directory on your `$PATH`. I should add a `setup.py` or something that does this for you, but I'm not sure the best way to do that yet.

## Todo

- [ ] Check to see if this works in Python 3
- [ ] This should probably be packaged better
- [ ] There should be a smarter way to find source or text files instead of the exclusions
- [ ] Colorization is specific to light-on-dark terminal color schemes
