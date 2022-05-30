#!/usr/bin/python3
"""lass MyList that inherits from list"""


class MyList(list):
    """"class"""

    def print_sorted(self):
        """prints the list, but sorted"""
        print(sorted(self))
