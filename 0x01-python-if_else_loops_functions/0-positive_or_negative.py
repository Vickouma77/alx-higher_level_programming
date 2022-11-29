#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("number is positive {}".format(number))
elif number == 0:
    print("number is equal to zero {}".format(number))
else:
    print("number is negative {}".format(number))
