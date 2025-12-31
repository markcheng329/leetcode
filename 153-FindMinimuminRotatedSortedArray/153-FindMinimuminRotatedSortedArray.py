# Last updated: 12/31/2025, 3:18:40 AM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        l, r = 0 , len(nums)-1
4
5        if nums[l] < nums[r]:
6            return nums[l]
7        
8        while l < r:
9            mid = (l+r)//2
10            if nums[mid] > nums[r]:
11                l = mid +1
12            else:
13                r = mid
14        return nums[l]