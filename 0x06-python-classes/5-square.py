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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            """return the square"""
            self.__size = value

    def area(self):
        """size square"""
        return self.__size ** 2

    def my_print(self):
        """printing"""
        if self.__size == 0:
            print('')
        else:
            for i in range(self.__size):
                for b in range(self.__size):
                    print("#", end="")
                print('')
