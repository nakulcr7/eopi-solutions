
def reverse(x):
    '''
    Int -> Int
    Given: an integer x
    Returns: the same x, reversed
    '''
    result, x_remaining = 0, abs(x)

    while x_remaining:
        result = (result * 10) + x_remaining % 10
        x_remaining //= 10

    return -result if x < 0 else result


if __name__ == "__main__":
    assert reverse(12) == 21
    assert reverse(-12) == -21
