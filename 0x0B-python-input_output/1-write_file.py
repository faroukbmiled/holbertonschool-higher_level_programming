#!/usr/bin/python3
"""write_file"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and
    returns the number of characters written"""
    count = 0
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
