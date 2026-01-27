# Last updated: 1/27/2026, 2:41:38 AM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        dp = [0] * (len(s)+1)
4
5        dp[0] = 1
6        dp[1] = 1 if s[0] != "0" else 0
7
8        for i in range(2,len(s)+1):
9            if s[i-1] != "0":
10                dp[i] += dp[i-1]
11            
12            if 10 <= int(s[i-2:i]) <=26:
13                dp[i] += dp[i-2]
14
15        return dp[len(s)]