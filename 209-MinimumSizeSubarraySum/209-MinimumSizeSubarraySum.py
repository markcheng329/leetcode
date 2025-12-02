# Last updated: 12/2/2025, 2:48:55 AM
1class Solution:
2    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
3        l = 0
4        res = float("inf")
5        total = 0
6        
7        for i in range(len(nums)):
8            total += nums[i]
9            while total >= target:
10                res = min(res,i-l+1)
11                total -= nums[l]
12                l +=1
13
14        return 0 if res == float("inf") else res