# Last updated: 1/30/2026, 11:45:06 PM
1class Solution:
2    def firstMissingPositive(self, nums: List[int]) -> int:
3        n = len(nums)
4        i = 0
5
6        while i < n:
7            x = nums[i]
8            if 1<= x <= n and nums[x-1] != x:
9                nums[i],nums[x-1] = nums[x-1],nums[i] 
10            else:
11                i +=1
12        
13
14        for i in range(n):
15            if nums[i] != i+1:
16                return i+1
17        return n +1