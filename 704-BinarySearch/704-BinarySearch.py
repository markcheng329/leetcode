# Last updated: 1/2/2026, 4:33:17 AM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l, r = 0,len(nums)-1
4
5        while l <= r:
6            mid = (l+r) //2
7            if nums[mid] == target:
8                return mid
9            
10            if nums[mid] > target:
11                r = mid -1
12            else:
13                l = mid +1
14        return -1