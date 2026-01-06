# Last updated: 1/6/2026, 5:47:53 AM
1class Solution:
2    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
3        maxHeap = []
4        res = []
5        for x,y in points:
6            dis = -(x**2+y**2)
7            heapq.heappush(maxHeap,[dis,x,y])
8            if len(maxHeap)> k:
9                heapq.heappop(maxHeap)
10        
11        while maxHeap:
12            dis,x,y = heapq.heappop(maxHeap)
13            res.append([x,y])
14        return res