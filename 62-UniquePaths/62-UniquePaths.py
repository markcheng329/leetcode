# Last updated: 2/9/2026, 3:58:53 PM
1class Solution:
2    def uniquePaths(self, m: int, n: int) -> int:
3        dp = [[0]* n for i in range(m)]
4
5        for i in range(m):
6            dp[i][0] = 1
7        
8        for j in range(n):
9            dp[0][j] = 1
10        
11        for i in range(1,m):
12            for j in range(1,n):
13                dp[i][j] = dp[i-1][j] + dp[i][j-1]
14        
15        return dp[m-1][n-1]