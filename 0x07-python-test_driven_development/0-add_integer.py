#!/usr/bin/python3

def add_integer(a, b=98):
    """ adds 2 integers"""
    if type(a) not in [int, float]:
        raise TypeError("a must be a integer")
        return
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
        return
    return (int(a) + int(b))
