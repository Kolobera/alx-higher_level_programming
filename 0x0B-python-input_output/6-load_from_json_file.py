#!/usr/bin/python3
"""The to json string module"""
import json


def load_from_json_file(filename):
    """load obj from json file"""
    with open(filename, "r") as file:
        line = file.readlines()
        for i in line:
            return (json.loads(i))
