# Last updated: 1/20/2026, 3:59:34 AM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        best_l,best_len = 0,0
4
5        for i in range(len(s)):
6            l,r = i,i
7            while l >= 0 and r < len(s) and s[l] == s[r]:
8                if r-l + 1 > best_len:
9                    best_len = r-l+1
10                    best_l = l
11            
12                l-=1
13                r+=1
14    
15        for i in range(len(s)):
16            l,r = i,i+1
17            while l >= 0 and r < len(s) and s[l] == s[r]:
18                if r-l+1 > best_len:
19                    best_len = r-l+1
20                    best_l = l
21                l-=1
22                r+=1
23        return s[best_l:best_l+best_len]
24
25