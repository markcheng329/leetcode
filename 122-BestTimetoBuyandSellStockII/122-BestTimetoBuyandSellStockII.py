# Last updated: 2/1/2026, 9:36:19 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        res = 0
4
5        for i in range(1,len(prices)):
6            if prices[i-1] < prices[i]:
7                res += prices[i] - prices[i-1]
8        return res
9