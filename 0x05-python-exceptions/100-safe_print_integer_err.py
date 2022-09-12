#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    boo = True
    try:
        print("{:d}".format(value))
    except ValueError as err:
        boo = False
        sys.stderr.write("Exception: {}\n".format(err))
    except TypeError as err:
        boo = False
        sys.stderr.write("Exception: {}\n".format(err))
    return boo
