# Last updated: 11/25/2025, 1:24:07 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)):
            l, r = 0,len(nums)-1
            mid = (l+r)//2
        return nums[mid]