# Last updated: 11/30/2025, 4:55:36 AM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        l , r = 0, len(height)-1
4        res = 0
5
6        while l < r:
7            area = min(height[l],height[r]) * (r-l)
8            res = max(res,area)
9            if height[l] < height[r]:
10                l +=1
11            else:
12                r-=1
13        return res