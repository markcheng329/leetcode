# Last updated: 1/31/2026, 12:38:21 AM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        res,count = 0,0
4
5        for i in range(len(nums)):
6            if count == 0:
7                res = nums[i]
8            
9            if nums[i] == res:
10                count +=1
11            else:
12                count -=1
13        return res