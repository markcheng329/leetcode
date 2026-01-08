# Last updated: 1/8/2026, 2:50:15 AM
1class Solution:
2    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
3        minheap = []
4
5        intervals.sort(key=lambda x:x[0])
6
7        res = 0
8
9        for start,end in intervals:
10            if minheap and start >= minheap[0]:
11                heapq.heappop(minheap)
12            heapq.heappush(minheap,end)
13        return len(minheap)
14