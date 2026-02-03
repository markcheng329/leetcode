# Last updated: 2/2/2026, 8:02:53 PM
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
15                while l < r :
16                    total = nums[i] + nums[j] + nums[l] + nums[r]
17
18                    if total > target:
19                        r -=1
20                    elif total < target:
21                        l +=1
22                    else:
23                        res.append([nums[i],nums[j],nums[l],nums[r]])
24                        l +=1
25                        r -=1
26                        while l < r and nums[l] == nums[l-1]:
27                            l +=1
28                        while l < r and nums[r] == nums[r+1]:
29                            r -=1
30        return res