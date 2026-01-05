# Last updated: 1/4/2026, 8:14:38 PM
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
14        for s,h in stack:
15            res = max(res,(len(heights)-s)*h)
16        return res