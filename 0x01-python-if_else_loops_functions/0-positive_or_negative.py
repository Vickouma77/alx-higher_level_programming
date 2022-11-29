#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"number is positive {number}")
elif number == 0:
    print(f"number is equal to zero {number}")
else:
    print(f"number is negative {number}")
