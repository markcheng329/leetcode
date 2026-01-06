# Last updated: 1/6/2026, 6:04:54 AM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        maxheap = []
4        for num in nums:
5            if len(maxheap) < k:
6                heapq.heappush(maxheap, num)
7            else:
8                if num > maxheap[0]:
9                    heapq.heapreplace(maxheap, num)
10        return maxheap[0]