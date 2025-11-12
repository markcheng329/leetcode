# Last updated: 11/12/2025, 4:57:52 AM
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow2 = 0

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow