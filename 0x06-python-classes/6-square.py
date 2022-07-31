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
    
    @property
    def position(self):
        """getting position"""
        return self.__position

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

    @position.setter
    def position(self, value):
        """set position"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """size square"""
        return self.__size ** 2

    def my_print(self):
        """printing"""
        if self.__size == 0:
            print('')
        else:
            for i in range(self.__size):
                for a in range(self.__size):
                    print("#", end="")
                print('')
