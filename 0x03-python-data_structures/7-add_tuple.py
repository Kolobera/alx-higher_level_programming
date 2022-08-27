#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    la = []
    lb = []
    count_a = 0
    for i in tuple_a:
        if count_a <= 1:
            la.append(tuple_a[count_a])
            count_a += 1
    count_b = 0
    for i in tuple_b:
        if count_b <= 1:
            lb.append(tuple_b[count_b])
            count_b += 1
    for i in range(2 - count_a):
        la.append(0)
    for i in range(2 - count_b):
        lb.append(0)
    return la[0] + lb[0], la[1] + lb[1]
