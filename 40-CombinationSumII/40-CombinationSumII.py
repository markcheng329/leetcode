# Last updated: 1/12/2026, 7:26:36 PM
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
11            if remain < 0:
12                return
13            
14            for i in range(start,len(candidates)):
15                if i > start and candidates[i] == candidates[i-1]:
16                    continue
17                subset.append(candidates[i])
18                dfs(i+1,remain-candidates[i])
19                subset.pop()
20        dfs(0,target)
21        return res