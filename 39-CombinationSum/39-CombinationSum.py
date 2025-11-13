# Last updated: 11/13/2025, 6:11:39 AM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def backtracking(start,remain):
            if remain == 0:
                res.append(subset.copy())
            
            if remain < 0:
                return
            
            for i in range(start,len(candidates)):
                subset.append(candidates[i])
                backtracking(i,remain-candidates[i])
                subset.pop()
        
        backtracking(0,target)
        return res