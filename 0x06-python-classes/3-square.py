#!/usr/bin/python3
"""creating class Square
"""


class Square:
    """class square that defines a square
    """
    def __init__(self, size=0):
        """instantiating private instance attribute
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """return the current square area
        """
        return(size * size)
