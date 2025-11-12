# Last updated: 11/12/2025, 4:56:54 AM
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(2):
            for num in nums:
                res.append(num)
        return res