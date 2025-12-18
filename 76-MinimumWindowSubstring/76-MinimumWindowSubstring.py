# Last updated: 12/18/2025, 1:10:57 AM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        if len(t) >len(s):
4            return ""
5        
6        res = ""
7        l = 0
8        best_l = 0
9        best_length = float('inf')
10        missing = len(t)
11        count = Counter(t)
12        
13        for i in range(len(s)):
14            count[s[i]] -=1
15            if count[s[i]] >= 0 :
16                missing -=1
17            
18            while missing == 0:
19                if i-l +1 < best_length:
20                    best_length = i-l+1
21                    best_l = l
22                
23                count[s[l]] +=1
24                if count[s[l]] > 0:
25                    missing +=1
26                l +=1
27        return res if best_length == float("inf") else s[best_l:best_l+best_length]