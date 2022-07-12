#!/usr/bin/python3
"""Define the First Rectangle tha inherits from Base."""
base = __import__('base').Base 



class Rectangle(base):
    """Represent First Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id=None)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get/set width od the rectangle."""
        return (self.__width)
    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Get/set height of the rectangle."""
        return (self.__height)
    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """Get/set x of the rectangle."""
        return (self.__x)
    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Get/set y of the rectangle."""
        return (self.__y)
    @y.setter
    def y(self, value):
        self.__y = value
