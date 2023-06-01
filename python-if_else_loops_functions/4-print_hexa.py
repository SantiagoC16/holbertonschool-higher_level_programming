#!/usr/bin/python3
str = "{}"
for n in range(0, 99):
    hexn = hex(n)
    print(n, '=', str.format(hexn))
