# Last updated: 12/27/2025, 1:04:57 AM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        l, r = 0,len(height)-1
4
5        res = 0
6
7        while l < r:
8            area = min(height[l],height[r]) * (r-l)
9            res = max(res,area)
10
11            if height[l] < height[r]:
12                l +=1
13            else:
14                r-=1
15        return res