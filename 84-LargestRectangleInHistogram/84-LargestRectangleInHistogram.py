# Last updated: 11/12/2025, 4:59:08 AM
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index,height = stack.pop()
                res = max(res,(i-index)*height)
                start = index

            stack.append([start,heights[i]])

        
        for i, h in stack:
            res = max(res,(len(heights)-i)*h)
        return res