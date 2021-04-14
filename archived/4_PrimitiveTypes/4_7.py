def power(x, y):
    """
    Int Int -> Float
    Given: two integers x and y
    Returns: x to the power y
    """
    result, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x
    while power:
        if power & 1:
            result *= x
        x, power = (x * x), power >> 1
    return result


if __name__ == "__main__":
    assert power(2, 4) == 16
    assert power(2, 3) == 8
    assert power(-2, 3) == -8
    assert power(2, -1) == 0.5
    assert power(-2, -1) == -0.5
    assert power(3, 0) == 1
