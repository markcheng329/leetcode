# Last updated: 1/27/2026, 5:44:45 AM
1class Solution:
2    def canPartition(self, nums: List[int]) -> bool:
3        total = sum(nums)
4
5        if total % 2 == 1:
6            return False
7        
8        target = total //2
9
10        dp = [False] * (target+1)
11
12        dp[0] = True
13
14        for i in range(len(nums)):
15            for t in range(target,nums[i]-1,-1):
16                dp[t] = dp[t] or dp[t-nums[i]]
17        
18        return dp[target]