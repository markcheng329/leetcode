# Last updated: 1/21/2026, 5:11:55 AM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        return max(nums[0],self.rob2(nums[1:]),self.rob2(nums[:-1]))
4
5    def rob2(self,nums):
6        prev2,prev1 = 0,0
7        for i in range(len(nums)):
8            maxrob = max(prev2+nums[i],prev1)
9            prev2 = prev1
10            prev1 = maxrob
11        return prev1