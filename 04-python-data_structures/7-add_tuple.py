#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    my_list = [0, 0]
    for n in range(len(tuple_a)):
        if n >= 2:
            break
        my_list[n] += tuple_a[n]
    for m in range(len(tuple_b)):
        if m >= 2:
            break
        my_list[m] += tuple_b[m]
    tuple3 = (my_list[0], my_list[1])
    return tuple3
