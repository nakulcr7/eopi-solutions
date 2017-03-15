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
    # Test str_to_int
    print str_to_int("324"), type(str_to_int("324"))
    print str_to_int("-324"), type(str_to_int("-324"))

    # Test int_to_str
    print int_to_str(324), type(int_to_str(324))
    print int_to_str(-324), type(int_to_str(-324))


if __name__ == '__main__':
    main()
