#!/usr/bin/python3
""" Square Module """


class Square:
    """ Square Class """
    def __init__(self, __size=0):
        """ size of square """
        self.__size = __size
        if type(__size) != int:
            raise TypeError('size must be an integer')
        if __size < 0:
            raise ValueError('size must be >= 0')
