# Last updated: 1/6/2026, 5:56:48 AM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        minheap = (nums)
4        
5        heapq.heapify(minheap)
6
7        while len(minheap) > k:
8            heapq.heappop(minheap)
9        
10        return minheap[0]