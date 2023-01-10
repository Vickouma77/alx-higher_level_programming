#!/usr/bin/python3

"""defines a class that defines students"""


class Student:
    """class of Student
    """

    def __init__(self, first_name, last_name, age):
        """Defines instation of class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            """Method returns directory description"""
            return self.__dict__.copy()
