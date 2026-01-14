# Last updated: 1/14/2026, 3:01:19 AM
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
15                used[i] = True
16                subset.append(nums[i])
17                dfs()
18                subset.pop()
19                used[i] = False
20        dfs()
21        return res