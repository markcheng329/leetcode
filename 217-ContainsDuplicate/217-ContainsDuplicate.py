# Last updated: 12/17/2025, 9:13:16 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        seen = set()
4
5        for i in range(len(nums)):
6            if nums[i] in seen:
7                return True
8            else:
9                seen.add(nums[i])
10        return False