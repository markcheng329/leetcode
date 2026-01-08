# Last updated: 1/8/2026, 3:36:10 AM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        curres = 0
4        res = nums[0]
5
6        for num in nums:
7            if curres < 0:
8                curres = 0
9            curres += num
10            res = max(res,curres)
11        return res