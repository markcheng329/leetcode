# Last updated: 1/11/2026, 4:03:12 AM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        res = 0
4        rows = len(grid)
5        cols = len(grid[0])
6
7        def dfs(r,c):
8            if r < 0 or c < 0 or r>=rows or c>=cols or grid[r][c] == "0":
9                return None
10            
11            grid[r][c] = "0"
12            dfs(r+1,c)
13            dfs(r-1,c)
14            dfs(r,c+1)
15            dfs(r,c-1)
16        
17        for r in range(rows):
18            for c in range(cols):
19                if grid[r][c] == "1":
20                    dfs(r,c)
21                    res +=1
22        return res