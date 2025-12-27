# Last updated: 12/27/2025, 2:31:46 AM
1class Solution:
2    def minWindow(self, s: str, t: str) -> str:
3        if len(t) > len(s):
4            return ""
5
6        l = 0
7        best_l = 0
8        best_length = float("inf")
9        missing = len(t)
10        count = Counter(t)
11
12        for i in range(len(s)):
13            count[s[i]] -=1
14            if count[s[i]] >= 0:
15                missing -=1
16            
17            while missing == 0:
18                if i-l+1 < best_length:
19                    best_length = i-l+1
20                    best_l = l
21                
22                count[s[l]] +=1
23                if count[s[l]] > 0:
24                    missing +=1
25                l +=1
26        return "" if best_length == float("inf") else s[best_l:best_l+best_length]