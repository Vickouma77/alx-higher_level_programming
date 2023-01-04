#!/usr/bin/python3
def magic_string():
    magic_string.ntimes = getattr(magic_string, 'ntimes', 0) + 1
    return ("Holberton, " * (magic_string.ntimes - 1) + "BestSchool")
