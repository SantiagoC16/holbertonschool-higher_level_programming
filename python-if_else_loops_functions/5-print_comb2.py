#!/usr/bin/python3
str = "{}"
for n in range(0, 100):
    if n != 99:
        print(str.format(str(n).zfill(2)), ", ", end="")
print(str.format(str(n).zfill(2)))
