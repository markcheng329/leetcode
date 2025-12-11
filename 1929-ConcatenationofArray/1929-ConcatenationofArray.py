# Last updated: 12/10/2025, 8:43:36 PM
1class Solution:
2    def getConcatenation(self, nums: List[int]) -> List[int]:
3        res = [0] * len(nums) * 2
4        for i in range(len(nums)):
5            res[i] = nums[i]
6            res[i+len(nums)] = nums[i]
7        return res