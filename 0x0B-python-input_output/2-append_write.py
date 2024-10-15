#!/usr/bin/python3
""" Defines the function 'append_write' """


def append_write(filename="", text=""):
    """ Appends character/characters to a file """
    with open(filename, mode='a', encoding='utf-8') as a_file:
        num = a_file.tell()
        a_file.write(text)
        return a_file.tell() - num
