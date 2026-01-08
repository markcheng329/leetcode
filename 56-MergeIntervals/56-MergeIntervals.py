# Last updated: 1/8/2026, 2:23:18 AM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort(key=lambda x:x[0])
4        res = [intervals[0]]
5
6    
7        for start,end in intervals[1:]:
8            prev_end = res[-1][1]
9            if start > prev_end:
10                res.append([start,end])       
11            else:
12                res[-1][1] = max(res[-1][1],end)
13
14        return res