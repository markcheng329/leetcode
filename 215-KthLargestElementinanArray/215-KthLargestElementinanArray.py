# Last updated: 1/6/2026, 6:09:27 AM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        heap = []
4        for num in nums:
5            if len(heap) < k:
6                heapq.heappush(heap,num)
7            else:
8                if num > heap[0]:
9                    heapq.heapreplace(heap,num)
10        return heap[0]