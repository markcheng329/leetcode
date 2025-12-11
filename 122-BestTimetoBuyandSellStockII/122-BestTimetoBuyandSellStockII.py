# Last updated: 12/11/2025, 1:58:46 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        total = 0
4        
5        for i in range(1,len(prices)):
6            if prices[i] > prices[i-1]:
7                total += prices[i] - prices[i-1]
8        return total