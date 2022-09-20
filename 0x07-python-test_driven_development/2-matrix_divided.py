#!/usr/bin/python3
"""Matrix divide module"""


def matrix_divided(matrix, div):
    """Divide a matrix by div"""
    lp = []
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        if type(i) is not list or len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    for i in matrix:
        lp.append([round(x/div, 2) for x in i])
    return lp
