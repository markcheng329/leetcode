# Last updated: 1/6/2026, 6:01:31 AM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        minheap = (nums)
4        heapq.heapify(minheap)
5
6        while len(minheap) > k:
7            heapq.heappop(minheap)
8        
9        return minheap[0]