# Last updated: 1/28/2026, 11:55:32 AM
1class Solution:
2    def canPartition(self, nums: List[int]) -> bool:
3        total = sum(nums)
4        if total % 2 == 1:
5            return False
6        
7        target = total //2
8        dp = [False] * (target+1)
9        dp[0] = True
10        
11        for i in range(len(nums)):
12            for t in range(target,nums[i]-1,-1):
13                dp[t] = dp[t] or dp[t-nums[i]]
14        
15        return dp[target]
16