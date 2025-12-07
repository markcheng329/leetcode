# Last updated: 12/6/2025, 10:14:43 PM
1class Solution:
2    def getConcatenation(self, nums: List[int]) -> List[int]:
3        res = [0] * len(nums) * 2
4
5        for i in range(len(nums)):
6            res[i] = nums[i]
7            res [i+len(nums)] = nums[i]
8        return res