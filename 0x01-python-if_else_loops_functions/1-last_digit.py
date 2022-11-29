#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_2 = abs(number) % 10
number_2 = -number_2
if number_2 > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, number_2))
elif number_2 == 0:
    print("Last digit of {} is {} and is 0".format(number, number_2))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, number_2))
