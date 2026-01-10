# Last updated: 1/9/2026, 11:14:25 PM
1class Solution:
2    def partitionLabels(self, s: str) -> List[int]:
3        lastindex = {}
4        for i in range(len(s)):
5            c = s[i]
6            lastindex[c] = i
7        
8        size = 0
9        end = 0
10        res = []
11
12        for i in range(len(s)):
13            c = s[i]
14            size +=1
15            end = max(end,lastindex[c])
16
17            if i == end:
18                res.append(size)
19                size = 0
20        return res