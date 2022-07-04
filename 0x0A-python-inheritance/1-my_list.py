#!/usr/bin/python3
""" Define MyList that inherits from list"""


class MyList(list):
    """ subclass list """

    def __init__(self):
        """Initialize the object"""
        super().__init__()

    def print_sorted(self):
        """ Define methode to print list"""
        print(sorted(self))
