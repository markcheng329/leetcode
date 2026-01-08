# Last updated: 1/8/2026, 3:54:37 AM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        farthest = 0
4
5        for i in range(len(nums)):
6            if i > farthest:
7                return False
8            farthest = max(farthest,i+nums[i])
9        return True