# Last updated: 1/28/2026, 11:47:45 AM
1class Solution:
2    def lengthOfLIS(self, nums: List[int]) -> int:
3        tails = []
4
5        for i in range(len(nums)):
6            l,r = 0,len(tails)
7            while l < r:
8                mid = (l+r)//2
9                if nums[i] > tails[mid]:
10                    l = mid +1
11                else:
12                    r = mid
13                
14            
15            if l == len(tails):
16                tails.append(nums[i])
17            else:
18                tails[l] = nums[i]
19        return len(tails)