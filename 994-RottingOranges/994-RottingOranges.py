# Last updated: 11/12/2025, 10:51:24 PM
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        res = 0
        fresh = 0
        directions = [1,0],[-1,0],[0,1],[0,-1]
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    q.append((r,c))

        while fresh >  0 and q:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc] ==1):
                        grid[nr][nc] = 2
                        fresh -=1
                        q.append((nr,nc))
            res +=1
        return res if fresh == 0 else -1

