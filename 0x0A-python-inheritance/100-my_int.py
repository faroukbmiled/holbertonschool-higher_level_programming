#!/usr/bin/python3
"""New class"""


class MyInt(int):
    """ class MyInt that inherits from int"""

    def __eq__(self, other):
        return int(self) is not int(other)

    def __ne__(self, other):
        return int(self) == int(other)
