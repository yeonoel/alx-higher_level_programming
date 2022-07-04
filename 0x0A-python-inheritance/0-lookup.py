#!/usr/bin/python3

def lookup(obj):
    """ Return attributes and methodes of obj
    Args:
        obj(object): the object
    Return:
        Attrubutes and methode of obj
    """
    return (dir(obj))
