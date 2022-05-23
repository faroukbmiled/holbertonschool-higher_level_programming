#!/usr/bin/python3
""" this class define a Rectangle"""


class Rectangle:
    """Rectangle."""

    def __init__(self, width=0, height=0):
        """Initializer"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) is not int:
            TypeError("width must be an integer")
        if value < 0:
            ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) is not int:
            TypeError("height must be an integer")
        if value < 0:
            ValueError("height must be >= 0")
