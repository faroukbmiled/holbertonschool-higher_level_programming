#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ele = len(argv) - 1
    if ele == 0:
        print('0 arguments.')
    elif ele == 1:
        print('1 argument:')
        print('1: {:s}'.format(argv[1]))
    else:
        print("{:d} arguments:".format(ele))
        for i in range(ele):
            print('{:d}: {:s}'.format(i + 1, argv[i + 1]))
