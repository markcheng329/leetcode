# Last updated: 1/11/2026, 4:10:43 AM
1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        res = 0
4        rows = len(grid)
5        cols = len(grid[0])
6
7        def dfs(r,c):
8            if r < 0 or c < 0 or r>=rows or c>=cols or grid[r][c] == 0:
9                return 0
10
11            
12            area = 1
13            grid[r][c] = 0
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