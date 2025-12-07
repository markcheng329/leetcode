# Last updated: 12/6/2025, 11:53:18 PM
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        slow = 0
4
5        for i in range(len(nums)):
6            if nums[i] != val:
7                nums[slow] = nums[i]
8                slow +=1
9        return slow