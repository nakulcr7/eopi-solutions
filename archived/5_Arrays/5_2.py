# Main
def plus_one(A):
    """
    List -> List
    Given: Aa list representation of a number
    Returns: The given number + 1
    """
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


# Variant
def binary_sum(A, B):
    """
    List -> List
    Given: Two lists of the same length, representing numbers in binary
    Returns: Their sum
    """
    c = 0  # carry
    out = []
    for i in reversed(range(len(A))):
        # Full adder relation
        s = (A[i] ^ B[i]) ^ (c)
        c = (A[i] & B[i]) | (B[i] & c) | (A[i] & c)
        out.append(s)
    if c:
        out.append(c)
    out.reverse()
    return out


if __name__ == "__main__":
    # Plus One
    assert plus_one([1, 2, 9]) == [1, 3, 0]
    assert plus_one([9, 9, 9]) == [1, 0, 0, 0]

    # Binary Sum
    assert binary_sum([1, 0, 1], [1, 0, 1]) == [1, 0, 1, 0]
    assert binary_sum([1, 1, 1], [1, 1, 1]) == [1, 1, 1, 0]
