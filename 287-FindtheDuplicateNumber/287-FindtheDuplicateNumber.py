# Last updated: 1/5/2026, 2:40:27 AM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        seen = set()
4        for i in range(len(nums)):
5            if nums[i] in seen:
6                return nums[i]
7            else:
8                seen.add(nums[i])
9        