# Last updated: 1/27/2026, 2:45:42 AM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3
4        dp0 = 1
5        dp1 = 1 if s[0] != "0" else 0
6
7        for i in range(2,len(s)+1):
8            cur = 0
9            if s[i-1] != "0":
10                cur += dp1
11            
12            if 10 <= int(s[i-2:i]) <=26:
13                cur += dp0
14            
15            dp0,dp1 = dp1,cur
16
17        return dp1