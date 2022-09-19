#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    le = len(argv) - 1
    to_p = str(le)
    if le == 1:
        to_p += " argument:"
    elif le == 0:
        to_p += " arguments."
    else:
        to_p += " arguments:"
    print("{:s}".format(to_p))
    for i in range(1, le + 1):
        print("{:d}: {:s}".format(i, argv[i]))
