#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        my_list.sorted()
        return my_list[- 1]
    else:
        return None

