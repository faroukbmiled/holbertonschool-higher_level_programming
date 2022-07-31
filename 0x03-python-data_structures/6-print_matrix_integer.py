#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        size = len(i)
        add = 1
        for x in i:
            if size == add:
                print(f"{x}", end='')
            else:
                print(f"{x} ", end='')
            add = add + 1
        print("")
