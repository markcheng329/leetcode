# Last updated: 12/6/2025, 10:28:08 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        seen = {}
4
5        for i in range(len(nums)):
6            diff = target-nums[i]
7            if diff in seen:
8                return[seen[diff],i]
9            seen[nums[i]] = i
10        