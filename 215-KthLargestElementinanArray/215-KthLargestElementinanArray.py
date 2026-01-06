# Last updated: 1/6/2026, 5:55:48 AM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        maxheap = []
4        for num in nums:
5            heapq.heappush(maxheap,-num)
6        
7        while k-1 > 0:
8            heapq.heappop(maxheap)
9            k -=1
10        return -maxheap[0]