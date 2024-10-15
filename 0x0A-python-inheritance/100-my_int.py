#!/usr/bin/python3
""" Defines class MyInt that inherits fron class int """


class MyInt(int):
    """ reverses the comparison signs """
    def __init__(self, num):
        """ class MyInt constructor """
        self.num = num

    def __eq__(self, other):
        """ reverses the '==' sign """
        return self.num != other

    def __ne__(self, other):
        """ reverses the '!=' sign """
        return self.num == other

    def __str__(self):
        """ return an string """
        return "{:d}".format(self.num)
