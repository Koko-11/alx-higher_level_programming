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
