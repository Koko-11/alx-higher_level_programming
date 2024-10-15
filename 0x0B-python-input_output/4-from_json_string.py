#!/usr/bin/python3
""" Define the function 'from_json_string' """

import json


def from_json_string(my_str):
    """ converts json string to an object """
    return json.loads(my_str)
