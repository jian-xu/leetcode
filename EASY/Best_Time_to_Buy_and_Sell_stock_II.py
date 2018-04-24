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
        max_transaction = 0
        for price in prices:
            if (price <= min_in):
                max_profit += max_transaction
                min_in = price
                max_transaction = 0
            profit = price - min_in
            if (profit < max_transaction):
                max_profit += max_transaction
                min_in = price
                max_transaction = 0
            else:
                max_transaction = max(max_transaction, profit)
        max_profit += max_transaction
        return max_profit

