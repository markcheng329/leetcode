# Last updated: 1/22/2026, 4:36:44 AM
1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        rows,cols = len(grid),len(grid[0])
4        res = 0
5        directions = [1,0],[-1,0],[0,1],[0,-1]
6
7        def bfs(r,c):
8            q = deque()
9            grid[r][c] = 0
10            q.append((r,c))
11            area = 1
12            while q:
13                r,c = q.popleft()
14                for dr,dc in directions:
15                    nr,nc = r+dr,c+dc
16                    if nr not in range(rows) or nc not in range(cols) or grid[nr][nc] == 0:
17                        continue
18                    grid[nr][nc] = 0
19                    q.append((nr,nc))
20                    area +=1
21            return area
22
23        for r in range(rows):
24            for c in range(cols):
25                if grid[r][c] == 1:
26                    res = max(res,bfs(r,c))
27        return res