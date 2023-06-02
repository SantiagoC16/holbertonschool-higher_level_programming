#!/usr/bin/python3
for n in range(0, 10):
    for m in range (1, 10):
        if n == 0 and m == 1:
            print("{}{}".format(n, m), end="")
        elif m != n:
            print(", {}{}".format(n, m), end="")
print()