# Last updated: 1/28/2026, 6:47:50 PM
1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3        dp = [1] * n
4        for i in range(m-2,-1,-1):
5            for j in range(n-2,-1,-1):
6                dp[j]+=dp[j+1]
7        return dp[0]
8
9        