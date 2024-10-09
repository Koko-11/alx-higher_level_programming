#!/usr/bin/python3
""" Making a rectangle class """


class Rectangle:
    """ A rectangle class """

    def __init__(self, width=0, height=0):
        """ object initializer

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Function for getting the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ gets the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height of the rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
