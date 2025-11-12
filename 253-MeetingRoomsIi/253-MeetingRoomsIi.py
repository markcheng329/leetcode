# Last updated: 11/12/2025, 4:57:57 AM
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        minheap = []
        res = 0

        for start,end in intervals:
            while minheap and minheap[0] <= start:
                heapq.heappop(minheap)
            heapq.heappush(minheap,end)
            res = max(res,len(minheap))
        return res