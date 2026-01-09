# Last updated: 1/9/2026, 3:52:04 AM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        curSum = 0
4        res = nums[0]
5
6        for num in nums:
7            if curSum < 0:
8                curSum = 0
9            curSum += num
10            res = max(res,curSum)
11        return res