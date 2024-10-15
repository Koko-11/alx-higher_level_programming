#!/usr/bin/python3
""" Defines class 'Rectangle' that inherits from 'BaseGeometry' """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ inherits from BaseGeometry class """
    def __init__(self, width, height):
        """ class rectangle constructor """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ calculates the area of a rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ returns rectangle dimensions """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
