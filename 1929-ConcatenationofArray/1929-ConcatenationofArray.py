# Last updated: 11/24/2025, 10:16:58 PM
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]* n * 2

        for i in range(n):
            res[i] = nums[i]
            res[i+n] = nums[i]
        return res