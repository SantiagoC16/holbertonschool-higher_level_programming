#!/usr/bin/python3
the_str = "{:02d}"
for n in range(0, 100):
    if n != 99:
        print(the_str.format(n), ",", end=" ")
    else:
        print(the_str.format(n))
