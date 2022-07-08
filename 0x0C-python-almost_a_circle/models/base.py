#!/usr/bin/python3
"""Define a Base classe"""


class Base:
    """Represente The Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base class
        Arg:
            id(int): the id
        """
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
