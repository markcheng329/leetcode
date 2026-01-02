# Last updated: 1/2/2026, 4:30:52 AM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        stack = []
4        res = 0
5
6        for i in range(len(heights)):
7            start = i
8            while stack and stack[-1][1] > heights[i]:
9                index,height = stack.pop()
10                res = max(res,(i-index)*height)
11                start = index
12            stack.append([start,heights[i]])
13
14        for i, h in stack:
15            res = max(res,(len(heights)-i)*h)
16        
17        return res