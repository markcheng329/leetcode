# Last updated: 11/19/2025, 4:25:40 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in hashmap:
                return [hashmap[diff],i]
            else:
                hashmap[nums[i]] = i