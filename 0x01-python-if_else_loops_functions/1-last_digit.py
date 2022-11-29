#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_2 = abs(number) % 10
number_2 = -number_2
if number_2 > 5:
    print(f"Last digit of {number} is {number_2} and is greater than 5")
elif number_2 == 0:
    print(f"Last digit of {number} is {number_2} and is 0")
else:
    print(f"Last digit of {number} is {number_2} and is less than 6 and not 0")
