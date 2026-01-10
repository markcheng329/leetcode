# Last updated: 1/9/2026, 9:26:47 PM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        numSum = 0
4        res = nums[0]
5
6        for num in nums:
7            if numSum < 0:
8                numSum = 0
9            numSum += num
10            res = max(res,numSum)
11        return res