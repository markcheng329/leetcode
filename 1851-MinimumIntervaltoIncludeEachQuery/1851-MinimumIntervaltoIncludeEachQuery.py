# Last updated: 1/21/2026, 4:56:52 AM
1class Solution:
2    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
3        intervals.sort(key=lambda x:x[0])
4        res = {}
5        minheap = []
6        q = deque()
7        i = 0
8
9        for q in sorted(queries):
10            while i < len(intervals) and intervals[i][0] <= q:
11                l,r = intervals[i][0],intervals[i][1]
12                heapq.heappush(minheap,((r-l+1),r))
13                i +=1
14            
15            while minheap and minheap[0][1] < q:
16                heapq.heappop(minheap)
17            
18            res[q] = minheap[0][0] if minheap else -1
19
20        return [res[q] for q in queries]