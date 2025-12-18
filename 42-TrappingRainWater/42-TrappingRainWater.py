# Last updated: 12/18/2025, 12:22:35 AM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        l, r = 0,len(height)-1
4
5        lmax,rmax = height[l],height[r]
6        res = 0
7
8        while l < r:
9            if height[l] < height[r]:
10                l +=1
11                lmax = max(lmax,height[l])
12                res += lmax - height[l]
13            else:
14                r -=1
15                rmax = max(rmax,height[r])
16                res += rmax-height[r]
17        return res