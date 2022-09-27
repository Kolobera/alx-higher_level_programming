#!/usr/bin/python3
"""The adding attribute module"""


def add_attribute(obj, name, value):
    """Method that tests if it can add an attribute"""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
