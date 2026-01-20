# Last updated: 1/19/2026, 10:54:16 PM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        rows,cols = len(grid),len(grid[0])
4        res = 0
5        directions = [1,0],[-1,0],[0,1],[0,-1]
6
7        def dfs(r,c):
8            if r not in range(rows) or c not in range(cols) or grid[r][c] == "0":
9                return 
10            
11            grid[r][c] = "0"
12            for dr,dc in directions:
13                dfs(r+dr,c+dc)
14        
15        for r in range(rows):
16            for c in range(cols):
17                if grid[r][c] == "1":
18                    dfs(r,c)
19                    res +=1
20        return res