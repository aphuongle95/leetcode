"""You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.
    
Solution:
Apply this strategy:
Buy when the stock price decreases to the lowest (right before it increases again)
Sell when the stock price increases to the highest (right before it decreases again)

TODO: 
New strategy:
Iterate through the list
Check if the price is CONTINUOUSLY increasing or decreasing.
As soon as the pattern changes (decrease > increase or increase > decrease), sell or buy"""

from typing import List
import numpy as np
import unittest


class Solution:
    def diff(self, prices: List[int]) -> List[int]:
        diff = np.array(prices[1:]) - np.array(prices[:-1])
        return diff.tolist()

    def searchNextSell(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        diff = self.diff(prices)
        for i in range(len(diff)):
            if diff[i] < 0:
                return i
        return 0

    def searchNextBuy(self, prices: List[int]) -> int:

        diff = self.diff(prices)
        for i in range(len(diff)):
            if diff[i] > 0:
                return i
        return -1

    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        nextBuy = self.searchNextBuy(prices)
        if nextBuy == -1:
            return 0

        nextSell = self.searchNextSell(prices[nextBuy + 1 :]) + nextBuy + 1
        profit += prices[nextSell] - prices[nextBuy]
        profit += self.maxProfit(prices[nextSell:])

        return profit


class Test(unittest.TestCase):
    def test_by_stock(self):
        self.assertEqual(Solution().maxProfit([7, 1, 5, 3, 6, 4]), 7)
        self.assertEqual(Solution().maxProfit([1, 2, 3, 4, 5]), 4)
        self.assertEqual(Solution().maxProfit([7, 6, 4, 3, 1]), 0)


if __name__ == "__main__":
    unittest.main()
