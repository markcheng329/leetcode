# Last updated: 12/10/2025, 11:00:25 PM
1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        count = 0
4        res = 0
5        
6
7        for i in range(len(nums)):
8            if count == 0:
9                res = nums[i]
10            
11            if res != nums[i]:
12                count -=1
13            else:
14                count  +=1
15        return res
16