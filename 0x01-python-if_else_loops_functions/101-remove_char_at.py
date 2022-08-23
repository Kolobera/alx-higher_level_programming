#!/usr/bin/python3
def remove_char_at(str, n):
    new_s = ""
    for i in range(len(str)):
        if i != n:
            new_s += str[i]
    return new_s
