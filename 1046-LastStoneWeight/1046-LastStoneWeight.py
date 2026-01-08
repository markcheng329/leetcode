# Last updated: 1/7/2026, 7:26:51 PM
1class Solution:
2    def lastStoneWeight(self, stones: List[int]) -> int:
3        minheap = [-s for s in stones]
4        heapq.heapify(minheap)
5
6        while len(minheap) > 1:
7            y = -heapq.heappop(minheap)
8            x = -heapq.heappop(minheap)
9
10            if y != x:
11                heapq.heappush(minheap,-(y-x))
12        
13        return -minheap[0] if minheap else 0