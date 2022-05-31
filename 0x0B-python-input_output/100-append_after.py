#!/usr/bin/python3
"""append_after"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file,
    after each line containing a specific string
    """
    new = ""
    with open(filename) as read:
        for line in read:
            new += line
            if search_string in line:
                new += new_string
    with open(filename, "w") as write:
        write.write(new)
