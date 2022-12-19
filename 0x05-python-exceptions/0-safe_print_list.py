#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0

    try:
        while i < x:
            print(my_list[i], end=' ')
            i += 1
        print("\n")
    except IndexError:
        while True:
            try:
                print(my_list[i], end=' ')
                i += 1
            except IndexError:
                print("\n")
                return i
