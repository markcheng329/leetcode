# Last updated: 11/30/2025, 2:06:23 AM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        slow = 1
4
5        for fast in range(1,len(nums)):
6            if nums[fast] != nums[slow-1]:
7                nums[slow] = nums[fast]
8                slow +=1
9        return slow