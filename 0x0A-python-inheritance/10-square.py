#!/usr/bin/python3
"""The Square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The Square class"""
    def __init__(self, size):
        super().__init__(size, size)
