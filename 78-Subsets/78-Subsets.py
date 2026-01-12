# Last updated: 1/12/2026, 5:18:23 PM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        subset = []
4        res = []
5
6        def dfs(i):
7            if i == len(nums):
8                res.append(subset.copy())
9                return res
10            
11            subset.append(nums[i])
12            dfs(i+1)
13            subset.pop()
14            dfs(i+1)
15        
16        dfs(0)
17        return res