#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    to_r = [i for i in set_1 if i not in set_2]
    to_r += [j for j in set_2 if j not in set_1]
    return to_r
