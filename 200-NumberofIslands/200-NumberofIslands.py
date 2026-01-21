# Last updated: 1/21/2026, 5:41:57 AM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        rows,cols = len(grid),len(grid[0])
4        directions = [1,0],[-1,0],[0,1],[0,-1]
5        res = 0
6        q = deque()
7
8        def bfs(r,c):
9            grid[r][c] = "0"
10            q.append((r,c))
11
12            while q:
13                r,c = q.popleft()
14                for dr,dc in directions:
15                    nr,nc = r+dr,c+dc
16                    if nr not in range(rows) or nc not in range(cols) or grid[nr][nc] == "0":
17                        continue
18                    grid[nr][nc] = "0"
19                    q.append((nr,nc))
20            
21        
22        for r in range(rows):
23            for c in range(cols):
24                if grid[r][c] == "1":
25                    bfs(r,c)
26                    res +=1
27        return res