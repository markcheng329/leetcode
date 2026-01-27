# Last updated: 1/27/2026, 5:20:32 AM
1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int:
3        tails = []
4
5        for i in range(len(nums)):
6            l,r = 0,len(tails)
7            while l < r:
8                m = (l+r)//2
9                if nums[i] > tails[m]:
10                    l = m +1
11                else:
12                    r = m
13                
14            if l == len(tails):
15                tails.append(nums[i])
16            else:
17                tails[l] = nums[i]
18        return len(tails)