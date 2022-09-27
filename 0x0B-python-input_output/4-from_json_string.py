#!/usr/bin/python3
"""The to json string module"""
import json


def from_json_string(my_str):
    """returns object from json representation"""
    return json.loads(my_str)
