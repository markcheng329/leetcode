# Last updated: 11/12/2025, 4:56:58 AM
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        total = 0
        res = 0
    

        for i in range(len(nums)):
            total += nums[i]

            while (i-left+1) * nums[i] - total > k:
                total -= nums[left]
                left +=1
            
            res = max(res,i-left+1)
        return res

