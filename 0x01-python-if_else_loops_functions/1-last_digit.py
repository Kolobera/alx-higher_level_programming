#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = f"Last digit of {number} is "
if number >= 0:
    last_d = number % 10
else:
    last_d = number % 10 - 10
str += f"{last_d} "
if last_d > 5:
    str += "and is greater than 5"
elif last_d == 0:
    str += "and is 0"
else:
    str += "and is less than 6 and not 0"
print(str)
