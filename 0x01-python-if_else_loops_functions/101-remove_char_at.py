#!/usr/bin/python3
def remove_char_at(str, n):
    arr = str
    if n >= 0:
        arr = arr[:n] + arr[n+1:]
    return arr
