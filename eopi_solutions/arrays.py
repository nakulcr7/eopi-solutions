#!/usr/bin/env python3
from typing import List
import random

"""
5.1. The Dutch National Flag problem.

Write a program that takes an array `A` and index `i` into `A`, and rearrages
the elements such that all elements less than `A[i]`(the pivot) appear first,
followed by elements equal to the pivot, followed by elements greater than the pivot.
"""


def partition_array(A: List[int], i: int) -> List[int]:
    smaller, equal, larger = 0, 0, len(A)
    pivot = A[i]

    # Maintaining the below invariants.
    # - A[:smaller]: <A[i]
    # - A[smaller:equal]: =A[i]
    # - A[equal:larger]: unprocessed
    # - A[larger:]: >A[i]

    while equal < larger:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            A[larger], A[equal] = A[equal], A[larger]

    return A


"""
5.6. Buy and sell a stock once.

Write a program that takes an array denoting the daily stock price, and
returns the maximum profit that could be made by buying and then selling
one share of that stock. There is no need to buy if no profit is possible.
"""


def trade_single_stock(stock_prices: List[int]) -> int:
    min_price, profit = float("inf"), 0
    for price in stock_prices:
        profit = max(profit, price - min_price)
        min_price = min(min_price, price)
    return profit


"""
5.12. Sample offline data.

Implement an algorithm that takes as input an array of distinct elements and a
size, and returns a subset of the given size of the array elements. All subsets
should be equally likely. Return the result in input array itself.
"""

def random_subset(A: List[int], x: int) -> List[int]:
    if x == len(A):
        return A

    for i in range(x):
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
    
    return A
