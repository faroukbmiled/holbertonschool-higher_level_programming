#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    try:
        for index in range(0, x):
            print(my_list[index], end="")
            index += 1
        print()
        return x
    except IndexError:
        print()
        return index
