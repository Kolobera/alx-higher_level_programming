#!/usr/bin/python3
"""The Append after module"""


def append_after(filename="", search_string="", new_string=""):
    """append new string after search string"""
    with open(filename, "r") as file:
        data = file.readlines()
    lp = []
    for i in range(len(data)):
        lp.append(data[i])
        if search_string in data[i]:
            lp.append(new_string)

    with open(filename, "w") as file:
        file.write("".join(lp))
