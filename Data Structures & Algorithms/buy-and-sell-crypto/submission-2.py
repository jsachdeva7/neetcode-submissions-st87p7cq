class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Dynamic sliding window, no fixed length given in problem
        buy = 0
        profit = 0

        for sell in range(len(prices)):
            new_profit = prices[sell] - prices[buy]
            profit = max(profit, new_profit)
            if prices[sell] < prices[buy]:
                buy = sell
        return profit