from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    start = 0
    ans = 0
    for end in range(1, len(prices)):
        if prices[end] < prices[start]:
            start = end
        ans = max(ans, prices[end] - prices[start])

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
