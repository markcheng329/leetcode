# Last updated: 1/8/2026, 2:21:16 AM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort(key=lambda x:x[0])
4        res = [intervals[0]]
5        
6
7        for start,end in intervals[1:]:
8            prev_end = res[-1][1]
9            if start <= prev_end:
10                res[-1][1] = max(prev_end,end)
11            else:
12                prev_end = end
13                res.append([start,end])
14        return res