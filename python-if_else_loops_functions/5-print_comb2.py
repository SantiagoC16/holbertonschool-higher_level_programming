#!/usr/bin/python3
the_str = "{:02d}"
for n in range(0, 100):
    if n != 99:
        print("{}, ".format(n), end="")
    else:
        print("{}".format(n))
