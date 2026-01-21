# Last updated: 1/21/2026, 5:19:21 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        res = 0
4        low = float("inf")
5        
6        for i in range(len(prices)):
7            low = min(low,prices[i])
8            res = max(res,prices[i]-low)
9        return res
10