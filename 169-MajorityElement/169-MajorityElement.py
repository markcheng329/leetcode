# Last updated: 11/25/2025, 1:30:37 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 0

        for i in range(len(nums)):
            if count == 0:
                res = nums[i]
            
            if nums[i] == res:
                count +=1
            else:
                count -=1
        return res
                