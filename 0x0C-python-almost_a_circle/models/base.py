#!/usr/bin/python3

"""Writes the first class base"""

class Base:
    """A base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """instansciating id with value of none
        """

        if id is not none:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = id
