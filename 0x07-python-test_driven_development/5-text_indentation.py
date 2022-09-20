#!/usr/bin/python3

def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    for symb in ".:?":
        text = (symb + "\n\n"). join(
                        [line.strip(" ") for line in text.split(symb)])
    print(text, end="")
