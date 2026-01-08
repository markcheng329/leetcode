# Last updated: 1/8/2026, 1:39:10 AM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        minheap = []
4
5        for num in nums:
6            if len(minheap) < k:
7                heapq.heappush(minheap,num)
8            else:
9                if num > minheap[0]:
10                    heapq.heapreplace(minheap,num)
11        
12        return minheap[0]