# Last updated: 1/7/2026, 5:36:18 AM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort(key=lambda x:x[0])
4
5        res = [intervals[0]]
6
7        if not intervals:
8            return []
9        
10        for start,end in intervals:
11            prev_end = res[-1][1]
12            if prev_end >= start:
13                res[-1][1] = max(end,prev_end)
14            else:
15                res.append([start,end])
16        return res