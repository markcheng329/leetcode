# Last updated: 1/28/2026, 10:02:23 AM
1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        res = 0
4
5        for i in range(len(s)):
6            l,r = i,i
7            while l >= 0 and r< len(s) and s[l] == s[r]:
8                res +=1
9                l-=1
10                r+=1
11            
12            l,r = i,i+1
13            while l >= 0 and r < len(s) and s[l] == s[r]:
14                res +=1
15                l -=1
16                r+=1
17        return res