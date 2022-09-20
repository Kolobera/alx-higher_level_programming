#!/usr/bin/python3
"""The say my name module"""


def say_my_name(first_name, last_name=""):
    """Prints the name of a person"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
