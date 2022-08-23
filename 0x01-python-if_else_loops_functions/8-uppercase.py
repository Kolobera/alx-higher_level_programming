#!/usr/bin/python3
def uppercase(str):
    up_string = ""
    for c in str:
        if 65 <= ord(c) <= 90:
            up_string += c
        elif 97 <= ord(c) <= 122:
            up_string += chr(ord(c) - 32)
        else:
            up_string += c
    print("{:s}".format(up_string))
