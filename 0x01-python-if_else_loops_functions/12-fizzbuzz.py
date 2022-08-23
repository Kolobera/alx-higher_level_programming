#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            if i % 5 == 0:
                to_p = "FizzBuzz"
            else:
                to_p = "Fizz"
        elif i % 5 == 0:
            to_p = "Buzz"
        else:
            to_p = str(i)
        print("{:s}".format(to_p), end=" ")
