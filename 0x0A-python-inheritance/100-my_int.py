#!/usr/bin/python3
"""The my int module"""


class MyInt(int):
    """Myint class"""
    def __eq__(self, x):
        return super().__ne__(x)

    def __ne__(self, x):
        return super().__eq__(x)
