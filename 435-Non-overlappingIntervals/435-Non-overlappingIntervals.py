# Last updated: 1/8/2026, 2:29:57 AM
1class Solution:
2    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key=lambda x:x[0])
4        res = 0
5
6        prev_end = intervals[0][1]
7
8        for start,end in intervals[1:]:
9            
10            if start >= prev_end:
11                prev_end = end
12            else:
13                prev_end = min(prev_end,end)
14                res +=1
15        return res
16
17