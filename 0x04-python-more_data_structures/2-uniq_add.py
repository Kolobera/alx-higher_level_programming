#!/usr/bin/python3
def uniq_add(my_list=[]):
    mo = []
    for i in my_list:
        if i not in mo:
            mo.append(i)
    return sum(mo)
