#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_l = []
    temp = []
    if idx < 0 or idx > len(my_list) - 1:
        new_l = my_list.copy()
    else:
        new_l = my_list.copy()
        new_l[idx] = element
    return new_l
