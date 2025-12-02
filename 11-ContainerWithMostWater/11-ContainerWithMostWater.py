# Last updated: 12/2/2025, 12:21:01 AM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        res = 0
4
5        l, r = 0,len(height)-1
6
7        while l < r:
8            area = min(height[l],height[r]) * ( r-l)
9            res = max(area,res)
10            if height[l] < height[r]:
11                l +=1
12            else:
13                r-=1
14
15        return res