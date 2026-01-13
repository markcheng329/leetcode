# Last updated: 1/12/2026, 11:14:55 PM
1class Solution:
2    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4        res = []
5        subset = []
6
7        def dfs(start):
8            res.append(subset.copy())
9
10            for i in range(start,len(nums)):
11                if i > start and nums[i] == nums[i-1]:
12                    continue
13                subset.append(nums[i])
14                dfs(i+1)
15                subset.pop()
16        dfs(0)
17        return res