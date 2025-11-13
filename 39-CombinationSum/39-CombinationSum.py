# Last updated: 11/13/2025, 6:23:24 AM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def backtracking(start,remain):
            if remain == 0:
                res.append(subset.copy())
            
            for i in range(start,len(candidates)):
                if remain < 0:
                    return
                subset.append(candidates[i])
                backtracking(i,remain-candidates[i])
                subset.pop()
        
        backtracking(0,target)
        return res