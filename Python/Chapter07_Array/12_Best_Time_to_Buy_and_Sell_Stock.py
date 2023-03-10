# 121. Best Time to Buy and Sell Stock

import sys

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        output = 0
        min_price = sys.maxsize
        for price in prices:
            min_price = min(price, min_price)
            output = max(output, price - min_price)

        return output