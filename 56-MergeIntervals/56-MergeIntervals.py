# Last updated: 1/8/2026, 2:21:46 AM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort(key=lambda x:x[0])
4        res = [intervals[0]]
5
6        
7
8        for start,end in intervals[1:]:
9            prev_end = res[-1][1]
10            if start > prev_end:
11                prev_end = end
12                res.append([start,end])       
13            else:
14                res[-1][1] = max(res[-1][1],end)
15
16        return res