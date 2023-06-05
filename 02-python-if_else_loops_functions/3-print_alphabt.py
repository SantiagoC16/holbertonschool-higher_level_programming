#!/usr/bin/python3
str = "{}"
for alpha in range(97, 123):
    if alpha != 101 and alpha != 113:
        print(str.format(chr(alpha)), end="")
