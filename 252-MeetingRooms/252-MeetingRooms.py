# Last updated: 1/8/2026, 2:40:28 AM
1class Solution:
2    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
3        if not intervals:
4            return True
5
6        intervals.sort(key=lambda x:x[0])
7
8        prev_end = intervals[0][1]
9
10
11        for s,e in intervals[1:]:
12            if s < prev_end:
13                return False
14            else:
15                prev_end = e
16        return True
17