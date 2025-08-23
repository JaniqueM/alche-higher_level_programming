#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 97 <= ord(c) <= 122:   # if c is lowercase (a–z)
            c = chr(ord(c) - 32)  # convert to uppercase
        print("{}".format(c), end="")
    print()  # new line at the end
