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

    for c in s:
        n = (n * 10) + (ord(c) - ord("0"))
    
    return -n if is_negative else n


"""6.2 Base Conversion.

Write a program that performs base conversion. The input is a string, an integer
`b1`, and another integer `b2`. The string represents an integer in base `b1`.
The output should be th string representing the integer in base `b2`. For example
("615", 7, 13) should return "1A7".
"""

def base_conversion(s: str, b1: int, b2: int) -> str:
    is_negative = False
    if s[0] == "-":
        is_negative = True
        s = s[1:]
    hex_to_int = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    int_to_hex = {v: k for k, v in hex_to_int.items()}
    
    def get_decimal() -> int:
        n = 0
        for c in s:
            n = n*b1
            if c in hex_to_int:
                n += hex_to_int[c]
            n += (ord(c) - ord("0"))
        return n

    def num_to_b2(n: int) -> str:
        ret = []
        while True:
            rem = n%b2
            if rem in int_to_hex:
                ret.append(int_to_hex[rem])
            else:
                ret.append(chr(rem + ord("0")))
            n //= b2
            if n == 0:
                break
        return "".join(reversed(ret))

    dec_s = get_decimal()
    s = num_to_b2(dec_s)
    return ("-" if is_negative else "") + s
