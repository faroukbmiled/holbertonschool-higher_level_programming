#!/usr/bin/python3
"""
 returns True if the object is an instance of a class that inherited
"""


def inherits_from(obj, a_class):
    """
returns True if the object is an instance of a class that inherited
"""

    return issubclass(obj.__class__, a_class) and type(obj) is not a_class
