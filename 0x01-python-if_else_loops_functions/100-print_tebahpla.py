#!/usr/bin/python3
for i in reversed(range(97, 123)):
    if i % 2 == 1:
        to_p = chr(i - 32)
    else:
        to_p = chr(i)
    print("{:s}".format(to_p), end="")
