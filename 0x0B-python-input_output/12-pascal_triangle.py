#!/usr/bin/python3
"""The Pascal module"""


def pascal_triangle(n):
    """return pascal triangle"""
    if n <= 0:
        return []
    lp = []
    for i in range(n):
        if i == 0:
            lp.append([1])
        else:
            j = [0] + lp[-1] + [0]
            lm = [j[el] + j[el+1] for el in range(len(j) - 1)]
            lp.append(lm)

    return lp
