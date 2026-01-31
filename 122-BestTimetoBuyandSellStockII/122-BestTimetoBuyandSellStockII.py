# Last updated: 1/30/2026, 11:01:57 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        res = 0
4
5        for i in range(len(prices)-1):
6            if prices[i+1] > prices[i]:
7                res += prices[i+1] - prices[i]
8        return res