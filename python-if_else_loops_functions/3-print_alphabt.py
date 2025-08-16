#!/usr/bin/python3
for i in range(97, 123):  # a to z
    if i == 101 or i == 113:  # skip 'e' (101) and 'q' (113)
        continue
    print("{}".format(chr(i)), end="")
