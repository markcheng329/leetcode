# Last updated: 1/22/2026, 3:27:19 AM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        hashmap = {}
4        for i in range(len(nums)):
5            diff = target - nums[i]
6            if diff in hashmap:
7                return[hashmap[diff],i]
8            hashmap[nums[i]] = i
9        