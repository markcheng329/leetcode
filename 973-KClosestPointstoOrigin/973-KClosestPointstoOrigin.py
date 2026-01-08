# Last updated: 1/7/2026, 9:03:18 PM
1class Solution:
2    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
3        heap = []
4        res = []
5
6        for x,y in points:
7            dis = x**2 + y**2
8            heapq.heappush(heap,[-dis,x,y])
9            if len(heap) > k:
10                heapq.heappop(heap)
11        
12        while heap:
13            dis,x,y = heapq.heappop(heap)
14            res.append([x,y])
15        
16        
17        
18        return res
19        
20
21        
22