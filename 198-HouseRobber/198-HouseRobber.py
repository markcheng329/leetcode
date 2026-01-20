# Last updated: 1/20/2026, 3:47:55 AM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        prev2,prev1 = 0,0
4        for i in range(len(nums)):
5            maxrob = max(prev2+nums[i],prev1)
6            prev2 = prev1
7            prev1 = maxrob
8        return prev1