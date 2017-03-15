import math


def to_base10(num, input_base):
    base10 = 0
    i = 0
    while num > 0:
        digit = num % 10
        base10 += digit * int(math.pow(input_base, i))
        i += 1
        num /= 10
    return base10


def from_base10(num, output_base):
    new_num = 0
    return new_num


def str_to_int(s):
    if s.startswith("-"):
        mul = -1
        s = s[1:]
    else:
        mul = 1
    num = 0
    for c in s:
        num = num * 10 + int(c)
    return num * mul


def int_to_str(num):
    if num < 0:
        neg = True
        num = -num
    else:
        neg = False
    s = []
    while num > 0:
        digit = num % 10
        s.append(str(digit))
        num /= 10
    if neg:
        s.append("-")
    s.reverse()
    return ''.join(s)


def main():
    # Test to_base10
    print to_base10(1011, 2)
    print to_base10(111, 2)


if __name__ == '__main__':
    main()
