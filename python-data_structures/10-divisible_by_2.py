#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for n in my_list:
        if n % 2 == 0:
            new_list = new_list.append(True)
        if n % 2 != 0:
            new_list = new_list.append(False)
