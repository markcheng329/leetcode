# Last updated: 1/8/2026, 3:35:10 AM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        curSum = 0
4        res = nums[0]
5
6        for i in range(len(nums)):
7            if curSum < 0:
8                curSum = 0
9            curSum += nums[i]
10            res = max(res,curSum)
11        return res