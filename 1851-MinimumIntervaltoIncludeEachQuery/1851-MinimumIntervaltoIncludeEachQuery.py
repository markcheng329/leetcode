# Last updated: 1/18/2026, 7:27:26 AM
1class Solution:
2    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
3        intervals.sort(key=lambda x:x[0])
4        minheap = []
5        res = {}
6        i = 0
7
8        for q in sorted(queries):
9            while i < len(intervals) and intervals[i][0] <=q:
10                l,r = intervals[i][0],intervals[i][1]
11                heapq.heappush(minheap,((r-l+1),r))
12                i +=1
13            
14            while minheap and minheap[0][1] < q:
15                heapq.heappop(minheap)
16            
17            res[q] = minheap[0][0] if minheap else -1
18        return [res[q] for q in queries]