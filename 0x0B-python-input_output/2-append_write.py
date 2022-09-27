#!/usr/bin/python3
"""The append write file module"""


def write_file(filename="", text=""):
    """Append text into file"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
