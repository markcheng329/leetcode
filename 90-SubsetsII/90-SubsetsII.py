# Last updated: 11/13/2025, 6:18:27 AM
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def backtracking(start):
            res.append(subset.copy())

            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
            
                subset.append(nums[i])
                backtracking(i+1)
                subset.pop()
        
        backtracking(0)
        return res
