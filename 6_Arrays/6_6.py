def max_profit(stock_prices):
    min_so_far = float("inf")
    profit_max = 0
    for stock in stock_prices:
        profit_max = max(profit_max, stock - min_so_far)
        min_so_far = min(min_so_far, stock)
    return profit_max


def main():
    stock_prices = [310, 315, 275, 295, 260, 270, 290, 230, 250, 255]
    assert max_profit(stock_prices) == 30
