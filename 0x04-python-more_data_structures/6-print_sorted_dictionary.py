#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sor = sorted(a_dictionary)
    for i in sor:
        print("{}: {}".format(i, a_dictionary[i]))
