#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    items = 0
    for i in range(x):
        try:
            print(print"{}".format(my_list[i]), end=" ")
            items += 1
        except IndexError:
            break
        print("")
        return(items)
