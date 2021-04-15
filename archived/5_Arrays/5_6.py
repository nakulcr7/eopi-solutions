# Main
def buy_and_sell_stock_once(prices):
    """
    List -> Int
    Given: a list of stock prices
    Returns: the max profit that could be made
    """
    min_so_far, max_profit = float("inf"), 0.0
    for price in prices:
        min_so_far = min(min_so_far, price)
        max_profit = max(max_profit, price - min_so_far)
    return max_profit


# Variant
def longest_equal_subarray(nums):
    """
    List -> List
    Given: a list of ints
    Returns: the largest sublist of equal ints
    """
    result, a_so_far = [], []
    for num in nums:
        if a_so_far == [] or num == a_so_far[-1]:
            a_so_far.append(num)
        else:
            a_so_far = [num]
        if len(a_so_far) > len(result):
            result = list(a_so_far)
    return result


if __name__ == "__main__":
    # Max profit
    assert (
        buy_and_sell_stock_once(
            [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
        )
        == 30
    )

    # Longest Equal Subarray
    assert longest_equal_subarray([1, 2, 2, 2, 3, 3, 4, 4]) == [2, 2, 2]
