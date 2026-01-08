# Last updated: 1/8/2026, 2:51:04 AM
1class Solution:
2    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
3        minheap = []
4
5        intervals.sort(key=lambda x:x[0])
6
7
8        for start,end in intervals:
9            if minheap and start >= minheap[0]:
10                heapq.heappop(minheap)
11            heapq.heappush(minheap,end)
12        return len(minheap)
13