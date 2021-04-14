def parity_brute(x):
    count = 0
    while x:
        count ^= x & 1
        x >>= 1
    return count


def parity_opt1(x):
    count = 0
    while x:
        count ^= 1
        x = x & (x - 1)
    return count


def parity_opt2(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1


# Variants
# --------
# Write expressions that use bitwise operators, especially
# equality checks, and Boolean operators to do the following
# in O(1) time


# 1. Right propagate the rightmost set bit in x
# e.g, turns (01010000) to (01011111)
def right_propagate_setbit(x):
    return x | x - 1


# 2. Compute x mod a power of two
# e.g, 77 mod 64 = 13
def mod_by_power_2(x, div):
    return x & (div - 1)


# 3. Test if x is a power of 2
def is_power_2(x):
    return not (x & 1)


if __name__ == "__main__":
    # Main
    assert parity_brute(11) == 1
    assert parity_brute(3) == 0

    assert parity_opt1(11) == 1
    assert parity_opt1(3) == 0

    assert parity_opt2(11) == 1
    assert parity_opt2(3) == 0

    # Variants
    assert right_propagate_setbit(80) == 95

    assert mod_by_power_2(77, 64) == 13

    assert is_power_2(63) == False
    assert is_power_2(64) == True
