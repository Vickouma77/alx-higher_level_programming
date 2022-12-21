#!/usr/bin/python3
class Square:
    """Type class square"""
    def __init__(self, size=0):
        """Init the square classs
        Args:
        param1: size is the type int attribute to make it private
        """
        self.size = size

    @property
    def size(self):
        """get the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return (self.__size * self.__size)
