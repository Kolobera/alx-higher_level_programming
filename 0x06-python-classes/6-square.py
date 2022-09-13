#!/usr/bin/python3
"Defines a class Square"


class Square:
    """Class Square that defines a square
    
    Attributes:
    __size (int): size of a size of the square
    __position (tuple): position of the square in 2D"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        print([type(x) is int for x in value])
        if type(value) is not tuple or len(value) != 2 or [type(x) is int for x in value] != [True, True] or [x >= 0 for x in value] != [True, True]:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
