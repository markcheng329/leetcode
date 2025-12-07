# Last updated: 12/6/2025, 10:16:09 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        seen = set()
4
5        for i in range(len(nums)):
6            if nums[i] in seen:
7                return True
8            seen.add(nums[i])
9        return False