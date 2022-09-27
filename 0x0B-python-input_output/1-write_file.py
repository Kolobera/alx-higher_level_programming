#!/usr/bin/python3
"""The write file module"""


def write_file(filename="", text=""):
    """Write text into file"""
    with open(filename, "w") as file:
        file.write(text)
