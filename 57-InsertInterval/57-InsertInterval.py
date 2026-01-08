# Last updated: 1/8/2026, 2:14:34 AM
1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        res = []
4
5        i = 0
6
7        while i < len(intervals):
8            if intervals[i][1] < newInterval[0]:
9                res.append(intervals[i])
10                i +=1
11            else:
12                break
13        
14        while i < len(intervals):
15            if intervals[i][0] <= newInterval[1]:
16                newInterval[0] = min(intervals[i][0],newInterval[0])
17                newInterval[1] = max(intervals[i][1],newInterval[1])
18                i +=1
19            else:
20                break
21        res.append(newInterval)
22
23        while i < len(intervals):
24            res.append(intervals[i])
25            i +=1
26        
27        return res