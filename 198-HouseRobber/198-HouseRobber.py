# Last updated: 11/13/2025, 4:36:58 AM
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2 = 0,0
        for i in range(len(nums)):
            maxrob = max(rob1 + nums[i],rob2)
            rob1 = rob2
            rob2 = maxrob
        return rob2