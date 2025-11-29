# Last updated: 11/29/2025, 1:50:44 AM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        if not nums:
4            return 0
5            
6        slow = 1
7
8        for fast in range(1,len(nums)):
9            if nums[fast] != nums[slow-1]:
10                nums[slow] = nums[fast]
11                slow +=1
12        return slow