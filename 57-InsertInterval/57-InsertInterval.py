# Last updated: 1/7/2026, 3:12:00 AM
1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        res = []
4
5        intervals.sort(key=lambda x:x[0])
6
7        i = 0
8
9        while i < len(intervals):
10            if intervals[i][1] < newInterval[0]:
11                res.append(intervals[i])
12                i +=1
13            else:
14                break
15            
16        while i < len(intervals):
17            if intervals[i][0] <= newInterval[1]:
18                newInterval[0] = min(intervals[i][0],newInterval[0])
19                newInterval[1] = max(intervals[i][1],newInterval[1])
20                i +=1
21            else:
22                break
23        res.append(newInterval)
24
25        while i < len(intervals):
26            res.append(intervals[i])
27            i +=1
28        return res
29            
30
31
32