# Last updated: 11/29/2025, 2:36:37 AM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4        res  = []
5        for i in range(len(nums)-2):
6            if nums[i] > 0:
7                break
8            if i> 0 and nums[i] == nums[i-1]:
9                continue
10        
11            l, r = i +1 ,len(nums)-1
12
13            while l < r:
14                total = nums[i] + nums[l] + nums[r]
15                if total > 0:
16                    r -=1
17                elif total < 0:
18                    l +=1
19                else:
20                    res.append([nums[i],nums[l],nums[r]])
21                    l+=1
22                    r-=1
23                    while l < r and nums[l] == nums[l-1]:
24                        l +=1
25        return res
26
27
28
29