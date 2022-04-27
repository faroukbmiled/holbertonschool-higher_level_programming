#!/usr/bin/python3
for i in range(0, 100):
    n = i / 10
    x = i % 10
    if i == 89:
        print(f'{i:d}')
    elif n < x:
        print(f'{i:02d}', end=", ")
