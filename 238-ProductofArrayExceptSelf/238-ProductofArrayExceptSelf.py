# Last updated: 12/11/2025, 1:46:30 AM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        res = [0] * len(nums)
4        prefix = 1
5
6        for i in range(len(nums)):
7            res[i] = prefix
8            prefix = prefix * nums[i]
9        
10        postfix = 1
11
12        for i in range(len(nums)-1,-1,-1):
13            res[i] = res[i] * postfix
14            postfix = postfix * nums[i]
15
16        return res