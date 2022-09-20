#!/usr/bin/python3
"""The text indentation module"""


def text_indentation(text):
    """indentates a text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for symb in ".:?":
        text = (symb + "\n\n"). join(
                        [line.strip(" ") for line in text.split(symb)])
    print(text, end="")
