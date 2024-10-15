#!/usr/bin/python3
""" Defines class 'Square' """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ performs square arithmetic operations """
    def __init__(self, size):
        """ class Square constructor """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ returns area of a square """
        return self.__size * self.__size

    def __str__(self):
        """ returns a string of square dimenssions """
        return "[Rectangle] {:d}/{:d}".format(self.__size, self.__size)
