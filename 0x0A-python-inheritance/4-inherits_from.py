#!/usr/bin/python3
""" Define Only sub class of"""


def inherits_from(obj, a_class):
    """ check if an object is an instance of a class
        that inherited( directly or indirectly
    Args:
        obj(any): the object to test
        a_class(type): the classe type for match
    returns:
        True if if the ibject is an instance of a class that inherited
        (directly or indirectly) otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)
