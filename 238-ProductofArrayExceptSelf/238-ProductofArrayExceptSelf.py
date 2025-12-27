# Last updated: 12/27/2025, 12:25:10 AM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        res = [0] * len(nums)
4
5        prefix = 1
6        for i in range(len(nums)):
7            res[i] = prefix
8            prefix = prefix * nums[i]
9        
10        postfix = 1
11        for i in range(len(nums)-1,-1,-1):
12            res[i] = res[i] * postfix
13            postfix = postfix * nums[i]
14
15        return res