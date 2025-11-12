# Last updated: 11/12/2025, 4:59:20 AM
class Solution:
    def jump(self, nums: List[int]) -> int:
        cur_end = 0 
        res = 0
        far = 0

        for i in range(len(nums)-1):
            far = max(far,i+nums[i])
            if i == cur_end:
                cur_end = far
                res +=1
            
            if cur_end >= len(nums)-1:
                break
        return res