# Last updated: 12/2/2025, 12:29:59 AM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        l,r = 0,len(height)-1
4        res = 0
5        lmax,rmax = height[l],height[r]
6
7        while l < r:
8            if height[l] < height[r]:
9                l +=1
10                lmax = max(height[l],lmax)
11                res += lmax - height[l]
12            else:
13                r -=1
14                rmax = max(height[r],rmax)
15                res += rmax - height[r]
16        return res