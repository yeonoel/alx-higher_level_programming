#!/usr/bin/python3
"""werite to a file."""


def write_file(filename="", text=""):
    """Write a string to a text.
    Args:
        filename(file): the file name.
        text(str): the string write in the file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
