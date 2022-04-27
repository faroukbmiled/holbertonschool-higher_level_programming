#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        last = number % 10
    else:
        lastt = abs(number) % 10
    print(last_digit, end="")
    return last
