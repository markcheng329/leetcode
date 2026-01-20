# Last updated: 1/20/2026, 3:50:47 AM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        return max(nums[0],self.rob2(nums[1:]),self.rob2(nums[:-1]))
4    
5
6    def rob2(self,nums):
7        prev2,prev1 = 0,0
8        for i in range(len(nums)):
9            maxrob = max(prev2 + nums[i],prev1)
10            prev2 = prev1
11            prev1 = maxrob
12        return prev1