#!/usr/bin/env python3

"""6.1. Interconvert strings and integers.

Implement an integer to string conversion function, and a string to integer
conversion function.
"""

def int_to_str(i: int) -> str:
    is_negative = False
    if i < 0:
        is_negative = True
        i = -i
    
    ret = []
    while True:
        ret.append(chr(ord("0") + i%10))
        i //= 10
        if i == 0:
            break

    return ("-" if is_negative else "") + "".join(reversed(ret))


def str_to_int(s: str) -> int:
    is_negative = False
    if s[0] == "-":
        is_negative = True
        s = s[1:]
    
    n = 0

    for i, c in enumerate(s):
        n = (n * 10) + (ord(c) - ord("0"))
    
    return -n if is_negative else n
