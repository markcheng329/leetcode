# Last updated: 12/10/2025, 8:46:20 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        seen = set()
4        for i in range(len(nums)):
5            if nums[i] in seen:
6                return True
7            seen.add(nums[i])
8        return False