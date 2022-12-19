#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    printed = 0

    while i < x:
        try:
            print(my_list[i], end='')
            printed += 1

        except IndexError:

            break
        i += 1

        print()
        return printed
