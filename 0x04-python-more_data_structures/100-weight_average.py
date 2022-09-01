#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    som = 0
    coe = 0

    for i, j in my_list:
        som += i * j
        coe += j
    return som / coe
