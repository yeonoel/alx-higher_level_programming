#!/usr/bin/python3
"""Defines a class Square that inherits from BaseGeometry."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of Square."""
    def __init__(self, size):
        """Initialise a new Rectangle.

        Args:
            size(int): The size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
