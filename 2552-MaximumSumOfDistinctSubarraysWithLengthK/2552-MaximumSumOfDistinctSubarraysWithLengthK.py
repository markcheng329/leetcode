# Last updated: 11/12/2025, 4:56:50 AM
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cur_sum = max_sum = 0
        left = 0
        seen = set()

        for i in range(len(nums)):
            while nums[i] in seen:
                seen.remove(nums[left])
                cur_sum -= nums[left]
                left +=1
            
            seen.add(nums[i])
            cur_sum += nums[i]
        
            if i - left + 1 > k:
                seen.remove(nums[left])
                cur_sum -= nums[left]
                left +=1
            
            if i - left + 1 == k:
                max_sum = max(cur_sum,max_sum)
        return max_sum