# Last updated: 1/27/2026, 2:50:26 AM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n = len(s)
4
5        dp0 = 1
6        dp1 = 1 if s[0] != "0" else 0
7
8        for i in range(2,n+1):
9            cur = 0
10            if s[i-1] != "0":
11                cur += dp1
12            
13            if 10 <= int(s[i-2:i]) <= 26:
14                cur += dp0
15            
16            dp0,dp1 = dp1,cur
17        return dp1