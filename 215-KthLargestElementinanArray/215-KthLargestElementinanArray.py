# Last updated: 1/8/2026, 1:35:57 AM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        minheap = []
4
5        for num in nums:
6            heapq.heappush(minheap,num)
7
8            if len(minheap) > k:
9                heapq.heappop(minheap)
10        
11        return minheap[0]