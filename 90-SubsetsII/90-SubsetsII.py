# Last updated: 11/13/2025, 5:35:23 AM
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def backtracking(i):
            res.append(subset.copy())

            for j in range(i,len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
            
                subset.append(nums[j])
                backtracking(j+1)
                subset.pop()
        
        backtracking(0)
        return res
