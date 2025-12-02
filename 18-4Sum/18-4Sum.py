# Last updated: 12/1/2025, 11:37:19 PM
1class Solution:
2    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
3        nums.sort()
4        res = []
5        
6        for i in range(len(nums)):
7            if i > 0 and nums[i] == nums[i-1]:
8                continue
9            for j in range(i+1,len(nums)):
10                if j > i+1 and nums[j] == nums[j-1]:
11                    continue
12                
13                l , r = j+1,len(nums)-1
14                while l < r:
15                    total = nums[i] + nums[j] + nums[l] + nums[r]
16                    if total > target:
17                        r-=1
18                    elif total < target:
19                        l +=1
20                    else:
21                        res.append([nums[i],nums[j],nums[l],nums[r]])
22                        l +=1
23                        r -=1
24                        while l < r and nums[l] == nums[l-1]:
25                            l+=1
26                        while l < r and nums[r] == nums[r+1]:
27                            r -=1
28        return res
29