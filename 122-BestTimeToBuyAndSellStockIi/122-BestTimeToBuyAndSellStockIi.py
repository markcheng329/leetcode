# Last updated: 11/12/2025, 4:59:00 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        
        return profit
