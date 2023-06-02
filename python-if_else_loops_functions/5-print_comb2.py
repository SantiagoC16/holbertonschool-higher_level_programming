#!/usr/bin/python3
str = "{}"
for n in range(0, 100):
    if n != 100:
        print(str.format(n), ", ", end="")
