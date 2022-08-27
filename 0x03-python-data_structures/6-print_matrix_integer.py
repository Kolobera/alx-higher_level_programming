#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        count = 1
        for j in i:
            if count < len(j):
                print("{}".format(j), end=" ")
            else:
                print("{}".format(j))
            count += 1
