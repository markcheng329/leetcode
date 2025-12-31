# Last updated: 12/30/2025, 7:04:32 PM
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
14        for start,heights[i] in stack:
15            res = max(res,(len(heights)-start)*heights[i])
16            
17        return res
18
19
20                
21