#!/usr/bin/env python3
from typing import List


"""
5.1. Write a program that takes an array `A` and index `i` into `A`, and rearrages
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
5.6. Write a program that takes an array denoting the daily stock price, and
returns the maximum profit that could be made by buying and then selling
one share of that stock. There is no need to buy if no profit is possible.
"""

def trade_single_stock(stock_prices: List[int]) -> int:
    min_price, profit = float("inf"), 0
    for price in stock_prices:
        profit = max(profit, price - min_price)
        min_price = min(min_price, price)
    return profit

