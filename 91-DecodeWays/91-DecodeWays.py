# Last updated: 1/28/2026, 10:39:51 AM
1class Solution:
2    def numDecodings(self, s: str) -> int:
3        n = len(s)
4
5        if n == 0:
6            return 0
7        
8        dp0 = 1
9        dp1 = 1 if s[0] != "0" else 0
10
11        for i in range(2,n+1):
12            cur = 0
13
14            if s[i-1] != "0":
15                cur += dp1
16            
17            if 10 <= int(s[i-2:i]) <= 26:
18                cur += dp0
19            
20            dp0,dp1 = dp1,cur
21        return dp1