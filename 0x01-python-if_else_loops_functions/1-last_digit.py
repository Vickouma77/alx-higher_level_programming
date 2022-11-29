#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_2 = abs(number) % 10
if number < 0:
    number_2 = -number_2
print("Last digit of {} is {} and is ".format(number, number_2), end="")
if number_2 > 5:
    print("greater than 5")
elif number_2 == 0:
    print("0")
else:
    print("less than 6 and not 0")
