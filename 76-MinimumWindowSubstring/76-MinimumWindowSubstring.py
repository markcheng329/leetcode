# Last updated: 12/9/2025, 12:34:24 AM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        if not s or not t or len(t) > len(s):
4            return ""
5        
6        missing = len(t)
7        best_len = float('inf')
8        best_l = 0
9        count = Counter(t)
10        l = 0
11
12
13        for i in range(len(s)):
14            count[s[i]] -=1
15            if count[s[i]] >= 0:
16                missing -=1
17            
18            while missing == 0:
19                if i-l+1 < best_len:
20                    best_len = i-l+1
21                    best_l = l
22                
23                count[s[l]] +=1
24                if count[s[l]] > 0:
25                    missing +=1
26                l +=1
27        return "" if best_len == float("inf") else s[best_l:best_l+best_len]
28
29
30
31            
32