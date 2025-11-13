# Last updated: 11/13/2025, 6:30:38 AM
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        used = [False] * len(nums)

        def backtracking():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                used[i] = True
                subset.append(nums[i])
                backtracking()
                subset.pop()
                used[i] = False
            
        backtracking()
        return res

            
