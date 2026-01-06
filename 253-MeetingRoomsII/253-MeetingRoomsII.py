# Last updated: 1/6/2026, 4:08:04 AM
1class Solution:
2    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
3        intervals.sort(key=lambda x:x[0])
4        res = 0
5        minheap = []
6
7        for start,end in intervals:
8            while minheap and minheap[0] <= start:
9                heapq.heappop(minheap)
10            heapq.heappush(minheap,end)
11            res = max(res,len(minheap))
12        return res