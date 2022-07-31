#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ele = len(argv)
    i = 1
    if ele == 1:
        print("0 arguments.")
    elif ele == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(ele - 1))
        while i < ele:
            print("{}: {}".format(i, argv[i]))
            i += 1
