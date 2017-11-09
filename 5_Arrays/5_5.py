# Main
def dup_delete(A):
    """
    List -> List
    Given: a sorted list of nums
    Returns: the given list with duplicated deleted
    """
    w_i = 1
    for i in range(1, len(A)):
        if A[w_i - 1] != A[i]:
            A[w_i] = A[i]
            w_i += 1
    return A[:w_i]


# Variant #1
def delete_key(A, k):
    """
    List, Int -> List
    Given: a list of nums and a key
    Returns: the given list with all occurences of the key removed
    """
    w_i = 0
    for i in range(len(A)):
        if A[i] != k:
            A[w_i] = A[i]
            w_i += 1
    return A[:w_i]


# Variant 2
def conditional_delete(A, m):
    """
    List, Int -> List
    Given: a sorted list of integers and another integer m
    Returns: the given list such that if an element of the list
            occurs 'm' times, it is replaces by min(2, m) occurences
    """
    w_i = 1  # write index
    r_c = 1  # running count
    for i in range(1, len(A)):
        if A[w_i - 1] != A[i]:
            if r_c > 1:
                if r_c == m:
                    r_c = min(2, m)
                while r_c > 1:
                    A[w_i] = A[i - 1]
                    r_c -= 1
                    w_i += 1
            A[w_i] = A[i]
            w_i += 1
        else:
            r_c += 1
    return A[:w_i]


if __name__ == "__main__":
    # Delete duplicates
    assert(dup_delete([])) == []
    assert(dup_delete([2, 3, 5, 5, 7, 11, 11, 11, 13])) == [2, 3, 5, 7, 11, 13]

    # Delete key
    assert(delete_key([], 0) == [])
    assert(delete_key([2, 3, 5, 5, 7, 11, 11, 11, 13], 5)) == \
        [2, 3, 7, 11, 11, 11, 13]

    # Conditional deletion
    assert(conditional_delete([2, 3, 5, 5, 7, 11, 11, 11, 13], 2)) == \
        [2, 3, 5, 5, 7, 11, 11, 11, 13]
    assert(conditional_delete([2, 3, 5, 5, 7, 11, 11, 11, 13], 1)) == \
        [2, 3, 5, 5, 7, 11, 11, 11, 13]
    assert(conditional_delete([2, 3, 5, 5, 7, 11, 11, 11, 13], 3)) == \
        [2, 3, 5, 5, 7, 11, 11, 13]
