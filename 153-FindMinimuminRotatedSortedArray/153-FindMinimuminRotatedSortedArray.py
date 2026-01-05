# Last updated: 1/4/2026, 9:08:57 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        l, r = 0,len(nums)-1
4
5        while l < r:
6            mid = (l+r)//2
7
8            if nums[l] < nums[r]:
9                return nums[l]
10
11            if nums[mid] > nums[r]:
12                l = mid +1
13            else:
14                r = mid
15
16        return nums[l]