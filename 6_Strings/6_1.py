import functools
import string


def int_to_str(n):
    """
    Int -> String
    Given: an int
    Returns: given int as a string
    """
    is_neg = False
    if n < 0:
        n, is_neg = -n, True

    result = []
    while n > 0:
        result.append(chr(ord("0") + n % 10))
        n //= 10
    return ("-" if is_neg else "") + "".join(reversed(result))


def str_to_int(s):
    """
    String -> Int
    Given: a string representing an int
    Returns: the int equivalent of the given string
    """
    return functools.reduce(lambda acc, c: acc * 10 + (ord(c) - ord("0")),
                            s[s[0] == "-"],
                            0) * (-1 if s[0] == "-" else 1)


if __name__ == "__main__":
    assert int_to_str(12) == "12"
    assert int_to_str(-12) == "-12"

    assert str_to_int("12") == 12
    assert str_to_int("-12") == -12
