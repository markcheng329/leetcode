# Last updated: 1/28/2026, 11:13:45 AM
1class Solution:
2    def coinChange(self, coins: List[int], amount: int) -> int:
3        dp = [amount + 1] * ( amount + 1)
4        dp[0] = 0
5
6        for i in range(1,amount + 1):
7            for c in coins:
8                if i -c >= 0:
9                    dp[i] = min (dp[i],dp[i-c]+1)
10        return dp[amount] if dp[amount] != amount + 1 else -1