#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        l = 0
        for index in range(0, x):
            print(f'{my_list[index]}', end='')
            l += 1
        print()
        return x
    except IndexError:
        print()
        return index
