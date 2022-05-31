#!/usr/bin/python3
"""class Student"""


class Student:
    """defines a student 'based on 9-student.py'"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        my_dict = dict()

        if type(attrs) is list:
            for element in attrs:
                if type(element) is not str:
                    return self.__dict__

                if element in self.__dict__:
                    my_dict[element] = self.__dict__[element]

            return my_dict

        return self.__dict__
