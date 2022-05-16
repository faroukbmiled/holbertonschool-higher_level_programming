#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    l = 0
    try:
        for index in range(0, x):
            print(my_list[l], end="")
            l += 1
        print()
        return x
    except IndexError:
        print()
        return index
