# Last updated: 1/6/2026, 5:41:18 AM
1class Solution:
2    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
3        minheap = []
4        res = []
5
6        for x,y in points:
7            dis = x**2 + y**2
8            minheap.append([dis,x,y])
9        heapq.heapify(minheap)
10
11        while k > 0:
12            dis,x,y = heapq.heappop(minheap)
13            res.append([x,y])
14            k-=1
15        
16        return res
17