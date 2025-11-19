# Last updated: 11/18/2025, 10:39:52 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        res = 0

        while l < r:
            area = (r-l) * min(height[l],height[r])
            res = max(area,res)
            if height[l] < height[r]:
                l +=1
            else:
                r-=1
        return res
