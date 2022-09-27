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
student_1 = Student("John", "Doe", 23)
student_2 = Student("Bob", "Dylan", 27)

j_student_1 = student_1.to_json()
j_student_2 = student_2.to_json(['first_name', 'age'])
j_student_3 = student_2.to_json(['middle_name', 'age'])

print(j_student_1)
print(j_student_2)
print(j_student_3)
