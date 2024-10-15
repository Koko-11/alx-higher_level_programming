#!/usr/bin/python3
""" Defines function 'is_same_class(obj, a_class)' """


def is_same_class(obj, a_class):
    """ Checks  if the object is exactly an instance of the specified class """
    if type(obj) == a_class:
        return True
    else:
        return False
