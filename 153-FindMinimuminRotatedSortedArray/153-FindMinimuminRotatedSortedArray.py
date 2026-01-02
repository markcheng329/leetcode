# Last updated: 1/2/2026, 4:46:31 AM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        l, r = 0,len(nums)-1
4
5        if nums[l] < nums[r]:
6            return nums[l]
7
8        while l < r:
9            mid = (l+r)//2
10
11            if nums[mid] > nums[r]:
12                l = mid +1
13            else:
14                r = mid 
15        return nums[l]