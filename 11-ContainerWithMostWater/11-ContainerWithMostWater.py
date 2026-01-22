# Last updated: 1/22/2026, 3:32:23 AM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        res = 0
4        l,r = 0,len(height)-1
5        area = 0
6
7        while l < r:
8            area = min(height[l],height[r]) * (r-l)
9            res = max(res,area)
10
11            if height[l] < height[r]:
12                l +=1
13            else:
14                r -=1
15        return res
16