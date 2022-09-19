#!/usr/bin/python3
def no_c(my_string):
    new_l = ""
    for i in my_string:
        if i != "c" and i != "C":
            new_l += i
    return new_l
