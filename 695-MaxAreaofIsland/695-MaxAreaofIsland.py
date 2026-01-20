# Last updated: 1/19/2026, 10:57:29 PM
1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        rows,cols = len(grid),len(grid[0])
4        directions = [1,0],[-1,0],[0,1],[0,-1]
5        res = 0
6
7        def dfs(r,c):
8            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0:
9                return 0
10            
11            area = 1
12            grid[r][c] = 0
13            for dr,dc in directions:
14                area += dfs(r+dr,c+dc)
15            return area
16        
17        for r in range(rows):
18            for c in range(cols):
19                if grid[r][c] == 1:
20                    res = max(res,dfs(r,c))
21        return res