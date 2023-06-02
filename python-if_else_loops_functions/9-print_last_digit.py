#!/usr/bin/python3
def print_last_digit(number):
    pos = number
    if number < 0:
        pos = -number
    num = pos % 10
    print("{}".format(num), end="")
    return num