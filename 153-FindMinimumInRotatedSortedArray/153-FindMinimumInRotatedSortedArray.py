# Last updated: 11/12/2025, 4:58:48 AM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums)-1
    
        if nums[l] < nums[r]:
            return nums[l]

        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        
        return nums[r]