# Last updated: 11/12/2025, 4:59:10 AM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 2

        for fast in range(2,len(nums)):
            if nums[fast] != nums[slow-2]:
                nums[slow] = nums[fast]
                slow +=1
        return slow