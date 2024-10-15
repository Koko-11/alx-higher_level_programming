#!/usr/bin/python3
""" Defines the function 'read_file' """


def read_file(filename=""):
    """ This function reads data from a file and
    prints it to stdout """
    with open(filename, mode='r', encoding='utf-8') as a_file:
        print(a_file.read(), end='')
