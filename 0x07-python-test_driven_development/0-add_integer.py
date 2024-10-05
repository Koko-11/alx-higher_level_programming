#!/usr/bin/python3
"""
Define add_integer function
This functions adds two integer
It casts float to int when float is given before adding them
"""


def add_integer(a, b=98):
    """ Check if 'a' is either an integer or a float """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    """ Check if 'b' is either an integer or a float """
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

