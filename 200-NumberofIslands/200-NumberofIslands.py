# Last updated: 1/10/2026, 12:06:31 AM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        directions = [1,0],[-1,0],[0,1],[0,-1]
4        res = 0
5        rows = len(grid)
6        cols = len(grid[0])
7
8        def dfs(r,c):
9            if r < 0 or c<0 or r>=rows or c>=cols or grid[r][c] == "0":
10                return
11            
12            grid[r][c] = "0"
13            dfs(r+1,c)
14            dfs(r-1,c)
15            dfs(r,c+1)
16            dfs(r,c-1)
17        
18        for r in range(rows):
19            for c in range(cols):
20                if grid[r][c] == "1":
21                    dfs(r,c)
22                    res +=1
23        return res