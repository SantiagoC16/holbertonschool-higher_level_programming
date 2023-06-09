#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set(my_list)
    suma = 0
    for s in new_set:
        suma += s
    return suma
