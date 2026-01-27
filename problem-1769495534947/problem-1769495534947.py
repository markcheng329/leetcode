# Last updated: 1/27/2026, 1:32:14 AM
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
11
12                l -=1
13                r +=1
14            
15            l,r = i,i+1
16            while l >= 0 and r < len(s) and s[l] == s[r]:
17                if r-l+1 > best_len:
18                    best_len = r-l+1
19                    best_l = l
20
21                l -=1
22                r +=1
23        
24        return s[best_l:best_l+best_len]