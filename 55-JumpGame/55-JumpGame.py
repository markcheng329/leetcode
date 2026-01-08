# Last updated: 1/8/2026, 3:50:25 AM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        goal = len(nums)-1
4
5        for i in range(len(nums)-2,-1,-1):
6            if i + nums[i] >= goal:
7                goal = i
8        return True if goal == 0 else False