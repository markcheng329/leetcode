# Last updated: 1/27/2026, 5:26:05 AM
1class Solution:
2    def canPartition(self, nums: List[int]) -> bool:
3        total = sum(nums)
4        if total % 2 == 1:
5            return False
6        target = total // 2
7
8        dp = [False] * (target + 1)
9        dp[0] = True
10
11        for x in nums:
12            for t in range(target, x - 1, -1):
13                dp[t] = dp[t] or dp[t - x]
14
15        return dp[target]