# Last updated: 1/8/2026, 4:03:50 AM
1class Solution:
2    def jump(self, nums: List[int]) -> int:
3        cur_end = 0
4        res = 0
5        farthest = 0
6
7        for i in range(len(nums)-1):
8            farthest = max(farthest,i+nums[i])
9            if i == cur_end:
10                res +=1
11                cur_end = farthest
12            
13            if cur_end >= len(nums)-1:
14                break
15        return res