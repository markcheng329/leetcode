# Last updated: 1/14/2026, 2:48:38 AM
1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        res = []
4        subset = []
5
6        def dfs(start,remain):
7            if remain == 0:
8                res.append(subset.copy())
9                return
10            
11            if remain < 0 :
12                return None
13            
14            for i in range(start,len(candidates)):
15                subset.append(candidates[i])
16                dfs(i,remain-candidates[i])
17                subset.pop()
18        dfs(0,target)
19        return res