# Last updated: 12/9/2025, 12:54:40 AM
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
13                l, r = j+1,len(nums)-1
14
15                while l < r:
16                    total = nums[i] + nums[j] + nums[l] + nums[r]
17                    if total > target:
18                        r -=1
19                    elif total < target:
20                        l +=1
21                    else:
22                        res.append([nums[i],nums[j],nums[l],nums[r]])
23                        l +=1
24                        r-=1
25                        while l < r and nums[l] == nums[l-1]:
26                            l +=1
27                        while l < r and nums[r] == nums[r+1]:
28                            r -=1
29        return res