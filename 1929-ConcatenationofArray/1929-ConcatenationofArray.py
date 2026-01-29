# Last updated: 1/28/2026, 7:37:23 PM
1class Solution:
2    def getConcatenation(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        res = [0] * (2*n)
5
6        for i in range(len(nums)):
7            res[i],res[i+n]  = nums[i] , nums[i]
8        return res