class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        min_in = prices[0]
        max_profit = 0
        for price in prices:
            min_in = min(price, min_in)
            profit = price - min_in
            max_profit = max(max_profit, profit)
        return max_profit