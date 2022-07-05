#!/usr/bin/python3
"""Append to a file"""


def append_write(filename="", text=""):
    """Append a string at the end of a file
    Args:
        filename(str): the file name
        text(str): the string to add into the file
    Return:
        the numbers of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
