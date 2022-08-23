#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        l_dig = number % 10
    else:
        l_dig = 10 - number % 10
    print("{}".format(number), end="")
    return l_dig
