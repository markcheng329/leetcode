# Last updated: 1/14/2026, 2:51:51 AM
1class Solution:
2    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
3        candidates.sort()
4        res = []
5        subset = []
6
7        def dfs(start,remain):
8            if remain == 0:
9                res.append(subset.copy())
10                return
11            
12            if remain < 0:
13                return None
14            
15            for i in range(start,len(candidates)):
16                if i > start and candidates[i] == candidates[i-1]:
17                    continue
18                subset.append(candidates[i])
19                dfs(i+1,remain - candidates[i])
20                subset.pop()
21        dfs(0,target)
22        return res