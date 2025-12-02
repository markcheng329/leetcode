# Last updated: 12/2/2025, 1:03:42 AM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        low = float("inf")
4        res = 0
5         
6        for i in range(len(prices)):
7            low = min(low,prices[i])
8            res = max(res,prices[i]-low)
9        return res