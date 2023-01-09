#!/usr/bin/python3
#1-my_list.py
"""Define a class that inherits from list"""


class MyList(list):
    """class inherits attributes from class lists"""

    def print_sorted(self):
        """that prints the list, but sorted in ascending sort"""

        list_sorted = self.copy()
        list_sorted.sort()
        print(l_sorted)
