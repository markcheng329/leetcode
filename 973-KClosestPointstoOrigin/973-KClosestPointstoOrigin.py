# Last updated: 1/7/2026, 9:00:00 PM
1class Solution:
2    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
3        minheap = []
4        res = []
5
6        for x,y in points:
7            dis = x**2 + y**2
8            heapq.heappush(minheap,[dis,x,y])
9
10        while len(res) < k:
11            dis,x,y = heapq.heappop(minheap)
12            res.append([x,y])
13        
14        return res
15        
16
17        
18