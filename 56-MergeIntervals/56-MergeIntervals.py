# Last updated: 1/6/2026, 4:51:45 AM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort(key=lambda x:x[0])
4        res= [intervals[0]]
5
6        for start,end in intervals[1:]:
7            prev_end = res[-1][1]
8            if res and prev_end >= start:
9                res[-1][1] = max(end,prev_end)
10                
11            else:
12                res.append([start,end])
13
14        return res
15            