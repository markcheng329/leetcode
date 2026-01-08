# Last updated: 1/8/2026, 2:41:09 AM
1class Solution:
2    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
3        if not intervals:
4            return True
5
6        intervals.sort(key=lambda x:x[0])
7
8        
9        prev_end = intervals[0][1]
10
11        for start,end in intervals[1:]:
12  
13            if start < prev_end:
14                return False
15            else:
16                # start >= prev_end
17                prev_end = end
18        return True