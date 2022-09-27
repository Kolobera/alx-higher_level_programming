#!/usr/bin/python3
"""The write file module"""


def write_file(filename="", text=""):
    """Write text into file"""
    ln = 0
    for i in text:
        if i == "\n":
            ln += 5
    with open(filename, "w") as file:
        file.write(text)
    return len(text) + ln

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)