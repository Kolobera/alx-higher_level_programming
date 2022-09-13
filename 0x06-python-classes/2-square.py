#!/usr/bin/python3
"Defines a class Square"


class Square:
    """Square class with private instance attribute size(integer)"""
    def __init__(self, size=0):
        if type(size) is not int:
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        else:
            self.__size = size
