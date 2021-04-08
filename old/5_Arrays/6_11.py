from random import randint


def random_subset(array, k):
    for i, num in enumerate(array):
        if i >= k:
            break
        r = randint(i, len(array) - 1)
        array[i], array[r] = array[r], array[i]
    return array[:k]


def main():
    A = [3, 7, 5, 11]
    print "Original", A
    print random_subset(A, 3)
    print random_subset(A, 3)
    print random_subset(A, 3)
    print random_subset(A, 3)
    print random_subset(A, 3)
    print random_subset(A, 3)
    print random_subset(A, 3)
