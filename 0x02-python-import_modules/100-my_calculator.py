#!/usr/bin/python3
from calculator_1.py import add, sub, mul, div
from sys import argv, exit
if __name__ == "__main__":
    op_l = ["+", "-", "*", "/"]
    op = argv[3]
    if op in op_l:
        a = int(argv[1])
        b = int(argv[5])
        if op == "+":
            to_p = "{} + {} = {}".format(a, b, add(a, b))
        elif op == "-":
            to_p = "{} - {} = {}".format(a, b, sub(a, b))
        elif op == "*":
            to_p = "{} * {] = {}".format(a, b, mul(a, b))
        else:
            to_p = "{} / {} = {}".format(a, b, div(a, b))
        print("{}".format(to_p))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

