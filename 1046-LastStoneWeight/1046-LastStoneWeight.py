# Last updated: 1/6/2026, 5:26:05 AM
1class Solution:
2    def lastStoneWeight(self, stones: List[int]) -> int:
3        maxheap = [-s for s in stones]
4        heapq.heapify(maxheap)
5
6        while len(maxheap) > 1:
7            y = -heapq.heappop(maxheap)
8            x = -heapq.heappop(maxheap)
9
10            if y!=x:
11                heapq.heappush(maxheap,-(y-x))
12
13        return -maxheap[0] if maxheap else 0