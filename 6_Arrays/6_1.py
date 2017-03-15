# Dutch National Flag Problem

import random


def less(i, j):
    return i < j


def exch(A, i, j):
    pass
    return


def partition(A, lo, hi):
    i = lo + 1
    j = hi

    while True:
        while less(A[i], A[lo]):
            if i == hi:
                break
            i += 1

        while less(A[lo], A[j]):
            if j == lo:
                break
            j -= 1

        if i > j:
            break
        exch(A, i, j)

    A[j], A[lo] = A[lo], A[j]
    #exch(A, j, lo)
    return j


def sort(A):
    random.shuffle(A)
    sortHelper(A, 0, len(A) - 1)


def sortHelper(A, lo, hi):
    if hi <= lo:
        return
    j = partition(A, lo, hi)
    sortHelper(A, lo, j - 1)
    sortHelper(A, j, hi)

sort([5, 4, 3])
