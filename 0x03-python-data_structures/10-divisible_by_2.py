#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    lp = []
    for i in range(len(my_list)):
        lp.append(my_list[i] % 2 == 0)
    return lp
