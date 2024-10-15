#!/usr/bin/python3
""" Defines the class 'Student' """


class Student:
    """ Contains details for a student """
    def __init__(self, first_name, last_name, age):
        """ class constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance """
        d = dict()
        if attrs is None:
            return self.__dict__
        else:
            for item in attrs:
                if item in self.__dict__:
                    d[item] = self.__dict__[item]
        return d
