#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    l = 0
    for i in range(0, x):
        try:
            print(f'{my_list[i]}', end='')
            l += 1
        except:
            pass
    print('')
    return l
