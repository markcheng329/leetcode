# Last updated: 11/13/2025, 6:23:12 AM
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        subset = []

        def backtracking(start,remain):
            if remain == 0:
                res.append(subset.copy())
                return
            
            if remain < 0:
                return
            
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                subset.append(candidates[i])
                backtracking(i+1,remain-candidates[i])
                subset.pop()
        
        backtracking(0,target)
        return res