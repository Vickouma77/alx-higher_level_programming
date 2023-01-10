#!/usr/bin/python3
# 0-read_file.py

"""Describes a function that reads text files"""


def read_file(filename=""):
    """Function that reads text files

    Args:
        filename:filename

    Raises
        Exception: when the file can be opened

    """

    with open("filename", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')