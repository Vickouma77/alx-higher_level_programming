#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_2 = abs(number) % 10
if number_2 < 0:
    number_2 = -number_2
print(f"Last string of {number} is {number_2}")
if number_2 > 5:
    print("and is greater than 5")
elif number_2 == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
