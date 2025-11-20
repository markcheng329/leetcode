# Last updated: 11/19/2025, 7:27:38 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = postfix * res[i]
            postfix = postfix * nums[i]
        
        return res