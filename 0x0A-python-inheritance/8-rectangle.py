#!/usr/bin/python3
""" BaseGeometry"""


class BaseGeometry:
    """ the Geometry Base."""
    def __init__(self):
        """ Initialize BaseGeometry."""
        pass

    def area(self):
        """ Not yet Implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value.
        Args:
            name(string): geometry name.
            value(integer): the value of the BaseGeometry.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Representation of Rectangle."""
    def __init__(self, width, height):
        """Initialise Recatangle.
        Args:
            width(int): the widht of the Rectangle.
            height(int): The height of the Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
