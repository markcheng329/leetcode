# Last updated: 1/17/2026, 11:47:41 PM
1class Solution:
2    def orangesRotting(self, grid: List[List[int]]) -> int:
3        rows = len(grid)
4        cols = len(grid[0])
5        fresh = 0
6        res = 0
7        directions = [1,0],[-1,0],[0,1],[0,-1]
8        q = deque()
9
10        for r in range(rows):
11            for c in range(cols):
12                if grid[r][c] == 1:
13                    fresh +=1
14                elif grid[r][c] == 2:
15                    q.append((r,c))
16                
17        while fresh > 0 and q:
18            for i in range(len(q)):
19                r,c = q.popleft()
20                for dr,dc in directions:
21                    nr,nc = r+dr,c + dc
22                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
23                        grid[nr][nc] = 2
24                        fresh -=1
25                        q.append((nr,nc))
26            res +=1
27        
28        return res if fresh == 0 else -1
29