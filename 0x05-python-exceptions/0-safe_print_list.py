#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        l = 0
        for index in range(0, x):
            l = l + 1
            print(f'{my_list[index]}', end='')
        print("")
        return x
    except IndexError:
        print("")
        return index
