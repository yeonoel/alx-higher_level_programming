#!/usr/bin/python3
"""Define a class-object cheking function"""


def is_same_class(obj, a_class):
    """Test if it's exact the same object

    Args:
        obj(any): the oject element to test
        a_class(type): type exactly of object
    Returns:
        True if it's exactly the same type otherwise return False
    """

    if type(obj) == a_class:
        return (True)
    return (False)
