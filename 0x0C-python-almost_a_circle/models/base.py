#!/usr/bin/python3
"""Module that contains the class base"""
import json
import csv
import os.path

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
