#!/usr/bin/python3
""" Square Module """


class Square:
    """square class"""
    def __init__(self, size=0):
        """Initialize"""
        self.__size = size

    @property
    def size(self):
        """ value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ set the value of size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """square area"""
        return self.__size ** 2
