#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for i, j in a_dictionary.items():
            if j == value:
                del a_dictionary[i]
                break

    return (a_dictionary)
