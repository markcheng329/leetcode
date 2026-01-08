# Last updated: 1/8/2026, 4:37:54 AM
1class Solution:
2    def partitionLabels(self, s: str) -> List[int]:
3        lastindex = {}
4
5        for i in range(len(s)):
6            c = s[i]
7            lastindex[c] = i
8        
9        size = 0
10        res = []
11        end = 0
12
13        for i in range(len(s)):
14            c = s[i]
15            size +=1
16            end = max(end,lastindex[c])
17
18            if i == end:
19                res.append(size)
20                size = 0
21        return res
22        
23
24