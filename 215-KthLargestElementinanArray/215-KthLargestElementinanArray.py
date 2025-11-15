# Last updated: 11/14/2025, 8:37:33 PM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = []

        for i in range(len(nums)):
            heapq.heappush(maxheap,nums[i])
            while len(maxheap) > k:
                heapq.heappop(maxheap)      
        return maxheap[0]
