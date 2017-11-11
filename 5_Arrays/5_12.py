import random


def random_sampling(A, k):
    """
    Given: a list of distinct ints and a size n
    Returns: a random sample of size n
    """
    for i in range(k):
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
    return A[:k]

if __name__ == "__main__":
    assert len(random_sampling([3, 7, 5, 11], 3)) == 3