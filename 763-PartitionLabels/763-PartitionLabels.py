# Last updated: 1/11/2026, 3:57:29 AM
1class Solution:
2    def partitionLabels(self, s: str) -> List[int]:
3        lastindex = {}
4        for i in range(len(s)):
5            c = s[i]
6            lastindex[c] = i
7        
8        res = []
9        size = 0
10        end = 0
11        
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