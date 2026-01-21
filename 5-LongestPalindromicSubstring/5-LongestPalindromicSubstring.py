# Last updated: 1/21/2026, 5:15:01 AM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        best_l,best_len = 0,0
4
5        for i in range(len(s)):
6            l,r = i,i
7            while l >= 0 and r < len(s) and s[l] == s[r]:
8                if r-l+1 > best_len:
9                    best_len = r-l+1
10                    best_l = l
11                l-=1
12                r+=1
13            
14            l,r = i,i+1
15            while l >= 0 and r < len(s) and s[l] == s[r]:
16                if r-l+1 > best_len:
17                    best_len = r-l+1
18                    best_l = l
19                l-=1
20                r+=1
21        return s[best_l:best_l+best_len]