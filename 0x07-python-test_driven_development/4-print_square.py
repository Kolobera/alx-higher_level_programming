#!/usr/bin/python3
"""The print square module"""


def print_square(size):
    """Print a square of size : size"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    print("\n".join("#" * size for x in range(size)))
