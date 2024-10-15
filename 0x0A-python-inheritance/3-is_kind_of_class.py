#!/usr/bin/python3
""" Defines a function 'is_kind_of_class' """


def is_kind_of_class(obj, a_class):
    """ Checks whether an object is an instance of, or
    if the object is an instance of a class that inherited from
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
