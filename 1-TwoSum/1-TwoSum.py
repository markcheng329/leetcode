# Last updated: 1/21/2026, 5:16:46 AM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        hashmap = {}
4
5        for i in range(len(nums)):
6            diff = target - nums[i]
7            if diff in hashmap:
8                return [hashmap[diff],i]
9            hashmap[nums[i]] = i  
10        