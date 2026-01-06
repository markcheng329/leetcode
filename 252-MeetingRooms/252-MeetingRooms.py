# Last updated: 1/6/2026, 4:02:49 AM
1class Solution:
2    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
3        if not intervals:
4            return True
5
6        intervals.sort(key=lambda x:x[0])
7
8        prev_end = intervals[0][1]
9
10        for start,end in intervals[1:]:
11            if start < prev_end:
12                return False
13            else:
14                prev_end = end
15        return True