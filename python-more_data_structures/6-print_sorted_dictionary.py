#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorte = sorted(a_dictionary.items())
    for k, v in sorte:
        print("{}: {}".format(k, v))
