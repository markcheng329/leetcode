# Last updated: 12/30/2025, 8:44:58 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3
4        l, r = 0,len(nums)-1
5
6        while l <= r:
7            mid = (l+r)//2
8            if nums[mid] == target:
9                return mid
10            elif nums[mid] > target:
11                r = mid -1
12            else:
13                l = mid +1
14        return -1