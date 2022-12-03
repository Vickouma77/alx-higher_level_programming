#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation import add, sub

    if a < b:
        c = add(a, b)
        for i in range(6, 8):
            c = add(c, i)
        return(c)

        else:
            return(sub(a, b))
