#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)

    average = 0
    size = 0
    for t in my_list:
        average += (t[0] * t[1])
        size += (t[1])
    return (average / size)
