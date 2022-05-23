#!/usr/bin/python3

"""
This module creates a class called Rectangle.
"""


class Rectangle:
    """rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        str = ""
        if self.__width != 0 or self.__height != 0:
            for row in range(self.__height):
                for col in range(self.__width):
                    str += '#'
                if row < self.__height - 1:
                    str += '\n'
            return str
        else:
            return ""

    def __repr__(self):
        return 'Rectangle(%s, %s)' % (self.__width, self.__height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print('Bye rectangle...')
