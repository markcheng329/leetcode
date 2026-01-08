# Last updated: 1/8/2026, 4:59:21 AM
1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        rows = len(grid)
4        cols = len(grid[0])
5        res = 0
6        area = 0
7
8        def dfs(r,c):
9            if r >= rows or c >= cols or grid[r][c] == 0 or r<0 or c<0:
10                return 0
11                
12            grid[r][c] = 0
13            area = 1
14            area += dfs(r+1,c)
15            area += dfs(r-1,c)
16            area += dfs(r,c+1)
17            area += dfs(r,c-1)
18            return area
19            
20        for r in range(rows):
21            for c in range(cols):
22                if grid[r][c] == 1:
23                    res = max(res,dfs(r,c))
24        return res
25            