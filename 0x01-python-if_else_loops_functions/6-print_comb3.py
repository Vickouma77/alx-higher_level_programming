#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i+1, 10):
        if i == j and j == i:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
