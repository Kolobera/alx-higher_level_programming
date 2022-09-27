#!/usr/bin/python3
"""The read file module"""


def read_file(filename=""):
    """print content of a file"""
    with open(filename, "r") as file:
        lines = file.readlines()
    for i in lines:
        print(i, end="")
