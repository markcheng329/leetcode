# Last updated: 1/11/2026, 3:41:20 AM
1class Solution:
2    def jump(self, nums: List[int]) -> int:
3        cur_end = 0
4        res = 0 
5        far = 0
6
7        for i in range(len(nums)-1):
8            far = max(far,i+nums[i])
9            if i == cur_end:
10                res +=1
11                cur_end = far
12        return res