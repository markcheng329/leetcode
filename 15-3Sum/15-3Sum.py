# Last updated: 12/18/2025, 12:17:12 AM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4        res = []
5
6        for i in range(len(nums)):
7            if nums[i] > 0 :
8                break          
9            if i > 0 and nums[i] == nums[i-1]:
10                continue
11            
12            l,r = i+1,len(nums)-1
13            
14            while l < r:
15                total = nums[i] + nums[l] + nums[r]
16                if total > 0:
17                    r-=1
18                elif total < 0:
19                    l +=1
20                else:
21                    res.append([nums[i],nums[l],nums[r]])
22                    l +=1
23                    r-=1
24                    while l < r and nums[l] == nums[l-1]:
25                        l +=1
26        return res
27            