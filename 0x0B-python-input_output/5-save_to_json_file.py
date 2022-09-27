#!/usr/bin/python3
"""The to json string module"""
import json


def save_to_json_file(my_obj, filename):
    """save json representation of
    my_obj in filename"""
    with open(filename, "w", encoding="Utf-8") as file:
        file.write(json.dumps(my_obj))
