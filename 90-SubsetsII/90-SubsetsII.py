# Last updated: 11/13/2025, 5:31:55 AM
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()          
        res = []
        subset = []

        def backtrack(i):
            res.append(subset.copy())
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue

                # 选择 nums[i]
                subset.append(nums[j])
                # 继续往后选，下一层从 i+1 开始
                backtrack(j + 1)
                # 撤销选择
                subset.pop()

        backtrack(0)
        return res