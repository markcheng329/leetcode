# Last updated: 1/6/2026, 4:52:55 AM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort(key=lambda x:x[0])
4        res= [intervals[0]]
5
6        if not intervals:
7            return []
8
9        for start,end in intervals[1:]:
10            prev_end = res[-1][1]
11            if prev_end >= start:
12                res[-1][1] = max(end,prev_end)
13                
14            else:
15                res.append([start,end])
16
17        return res
18            