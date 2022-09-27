#!/usr/bin/python3
"""The Student module"""


class Student:
    """Class representing students"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        lp = {}
        if attrs is not None and attrs != []:
            for i in attrs:
                if i in self.__dict__.keys():
                    lp[i] = self.__dict__[i]
        else:
            lp = self.__dict__
        return lp
