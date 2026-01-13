# Last updated: 1/12/2026, 7:46:32 PM
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        res = []
4        subset = []
5        used = [False] * len(nums)
6
7        def dfs():
8            if len(subset) == len(nums):
9                res.append(subset.copy())
10                return
11            
12            for i in range(len(nums)):
13                if used[i] == True:
14                    continue
15                
16                used[i] = True
17                subset.append(nums[i])
18                dfs()
19                subset.pop()
20                used[i] = False
21        dfs()
22        return res
23
24
25