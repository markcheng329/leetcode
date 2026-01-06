# Last updated: 1/6/2026, 4:58:17 AM
1class Solution:
2    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key=lambda x:x[0])
4        res = 0
5
6        prev_end = intervals[0][1]
7
8        for start,end in intervals[1:]:
9            if prev_end > start:
10                prev_end = min(prev_end,end)
11                res +=1
12            else:
13                prev_end = end
14        return res
15            