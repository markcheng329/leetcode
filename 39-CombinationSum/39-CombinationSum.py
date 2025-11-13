# Last updated: 11/13/2025, 6:06:59 AM
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
                val = candidates[i]
                subset.append(val)
                backtracking(i,remain-val)
                subset.pop()
        
        backtracking(0,target)
        return res