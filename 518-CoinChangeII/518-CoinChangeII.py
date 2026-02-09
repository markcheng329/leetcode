# Last updated: 2/9/2026, 5:24:22 PM
1class Solution:
2    def change(self, amount: int, coins: List[int]) -> int:
3        dp = [0] * (amount + 1)
4        dp[0] = 1
5
6        for c in coins:
7            for x in range(c, amount + 1):
8                dp[x] += dp[x - c]
9
10        return dp[amount]