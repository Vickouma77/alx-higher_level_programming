#!/usr/bin/python
#1-my_list.py
"""Define a class that inherits from list"""


class MyList(list):
    """class inherits attributes from class lists"""

    def print_sorted(self):
        """that prints the list, but sorted in ascending sort"""

        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
