#!/usr/bin/python3
"""creating class Square
"""


class Square:
    """class Square that defines a square
    """
    def __init__(self, size=0):
        """instantiating of Private instance attribute
        """
        self.size = size

    @property
    def size(self):
        """get the size of the square
        """
        return(self.__size)

    @size.setter
    def size(self, value):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """returns the current square area
        """
        return(self.__size * self.__size)
