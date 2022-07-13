#!/usr/bin/python3
"""Define the First Rectangle tha inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """Represent First Rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get/set width od the rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/set height of the rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get/set x of the rectangle."""
        return (self.__x)

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get/set y of the rectangle."""
        return (self.__y)

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the Area of the Rectangle."""
        return (self.width * self.height)

    def display(self):
        """ print in stdout the Rectangle."""
        if self.width == 0 or self.height == 0:
            print()
            return

        [print() for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for p in range(self.x)]
            [print("#", end='') for j in range(self.width)]
            print()

    def __str__(self):
        """Return the Rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str((self.id)) + ") "
        string += str(self.x) + "/" + str(self.y) + " - "
        string += str(self.width) + "/" + str(self.height)
        return (string)

    def update(self, *args):
        """assign argument to each attribute"""
        if (args) and len(args) != 0:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                elif i == 1:
                    self.width = v
                elif i == 2:
                    self.height = v
                elif i == 3:
                    self.x = v
                elif i == 4:
                    self.y = v
