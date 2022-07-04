#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Representation of Rectangle."""
    def __init__(self, width, height):
        """Initialise a new Rectangle.

        Args:
            width(int): the widht of the Rectangle.
            height(int): The height of the Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Return the area Rectangle."""
        return (self.__width * self.__height)

    def __str__(self):
        """ Return the print() and str()
            representation of the Rectangle.
        """
        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)
        return (string)
