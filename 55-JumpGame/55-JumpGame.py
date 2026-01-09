# Last updated: 1/9/2026, 3:55:24 AM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        far = 0
4
5        for i in range(len(nums)):
6            if i > far:
7                return False
8            far = max(far,i+nums[i])
9        return True