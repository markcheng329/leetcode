# Last updated: 11/14/2025, 10:03:23 PM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def backtracking(start,remain):
            if remain == 0:
                res.append(path.copy())
            
            if remain < 0:
                return
            
            for i in range(start,len(candidates)):

                path.append(candidates[i])
                backtracking(i,remain-candidates[i])
                path.pop()
        
        backtracking(0,target)
        return res