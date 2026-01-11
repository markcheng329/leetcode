# Last updated: 1/11/2026, 3:39:59 AM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        far = 0
4
5        for i in range(len(nums)):
6            if i > far:
7                return False
8            far = max(far,i+nums[i])
9        return True