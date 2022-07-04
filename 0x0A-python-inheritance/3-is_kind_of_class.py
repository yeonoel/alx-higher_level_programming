#!/usr/bin/python3
"""Define object-class cheking function"""


def is_kind_of_class(obj, a_class):
    """ Same class or inherit from
    Args:
        obj(any): the object to test
        a_class(type): the class object
    Return:
        True if the object is an instance of or id the object
        is an instance of class that inherited from, the specified class
        otherwise False
    """
    if isinstance(obj, a_class):
        return (True)
    return(False)
