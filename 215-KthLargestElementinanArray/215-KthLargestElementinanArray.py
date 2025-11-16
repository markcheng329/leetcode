# Last updated: 11/16/2025, 5:29:30 AM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = [-i for i in nums]
        heapq.heapify(maxheap)

        while (k-1)>0:
            heapq.heappop(maxheap)
            k-=1
            
        return -maxheap[0]
