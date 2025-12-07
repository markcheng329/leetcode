# Last updated: 12/7/2025, 12:00:46 AM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        res = 0
4        count = 0
5
6        for i in range(len(nums)):
7            if count == 0:
8                res = nums[i]
9            
10            if nums[i] == res:
11                count +=1
12            else:
13                count -=1
14
15        return res
16        