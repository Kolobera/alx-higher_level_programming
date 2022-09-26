#!/usr/bin/python3
"""The mylist module"""


class MyList(list):
    """My list class"""
    def print_sorted(self):
        l = self.copy()
        l.sort()
        print(l)