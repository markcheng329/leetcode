# Last updated: 1/13/2026, 9:14:22 PM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        res = []
4        subset = []
5
6        def dfs(start):
7            res.append(subset.copy())
8            
9            for i in range(start,len(nums)):
10                subset.append(nums[i])
11                dfs(i+1)
12                subset.pop()
13
14        dfs(0)
15        return res