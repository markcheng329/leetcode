# Last updated: 1/18/2026, 12:15:33 AM
1class Solution:
2    def orangesRotting(self, grid: List[List[int]]) -> int:
3        rows = len(grid)
4        cols = len(grid[0])
5        fresh = 0
6        res = 0
7        q = deque()
8
9        for r in range(rows):
10            for c in range(cols):
11                if grid[r][c] == 1:
12                    fresh +=1
13                elif grid[r][c] == 2:
14                    q.append((r,c))
15        
16        while fresh > 0 and q:
17            for i in range(len(q)):
18                r,c = q.popleft()
19                for dr,dc in [1,0],[-1,0],[0,1],[0,-1]:
20                    nr,nc = r+dr,c+dc
21                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
22                        grid[nr][nc] = 2
23                        fresh -=1
24                        q.append((nr,nc))
25            res +=1
26        
27        return res if fresh == 0 else -1