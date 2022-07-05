#!/usr/bin/python3
"""Read file."""


def read_file(filename=""):
    """Read text file UTF8 and prints.
    Arg:
        filename(file): the file that is read ant prints
    """
    with open(filename, encoding="utf-8") as f:
        text = f.read()
        print(text, end='')
