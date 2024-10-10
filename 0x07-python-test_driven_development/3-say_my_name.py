#!/usr/bin/python3
"""
Define function say_my_name
This function prints the full name
"""


def say_my_name(first_name, last_name=""):
    """ Fuction for printing the full name

    Args:
        first_name (str): First name
        last_name (str): Last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
