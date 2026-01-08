# Last updated: 1/8/2026, 6:05:54 AM
1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        rows = len(grid)
4        cols = len(grid[0])
5        res = 0
6
7        def dfs(r,c):
8            if r < 0 or c < 0 or r>=rows or c>=cols or grid[r][c] == 0:
9                return 0
10            
11            area = 1
12            grid[r][c] = 0
13            area += dfs(r+1,c)
14            area += dfs(r,c+1)
15            area += dfs(r-1,c)
16            area += dfs(r,c-1)
17            return area
18        
19        for r in range(rows):
20            for c in range(cols):
21                if grid[r][c] == 1:
22                    res = max (res, dfs(r,c))
23        return res