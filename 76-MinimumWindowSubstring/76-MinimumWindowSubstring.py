# Last updated: 12/6/2025, 9:55:07 PM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        if not s or not t or len(t) > len(s):
4            return ""
5        
6        l =0
7        best_l = 0
8        best_len = float("inf")
9        need = Counter(t)
10        missing = len(t)
11        
12        for i in range(len(s)):
13            need[s[i]] -=1
14            if need[s[i]] >= 0:
15                missing -=1
16            
17            while missing == 0:
18                if i-l+1 < best_len:
19                    best_len = i-l+1
20                    best_l = l
21                
22                need[s[l]] +=1
23                if need[s[l]] > 0:
24                    missing +=1
25                l +=1
26        return "" if best_len == float("inf") else s[best_l:best_l + best_len]
27        
28