# Last updated: 11/12/2025, 4:57:38 AM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        numsSet = set(nums)

        for i in range(1,len(nums)+1):
            if i not in numsSet:
                res.append(i)
        return res
