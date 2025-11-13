# Last updated: 11/12/2025, 8:23:27 PM
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        inf = 2**31-1
        rows,cols = len(rooms),len(rooms[0])
        q =deque()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r,c))
        
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in [1,0],[-1,0],[0,1],[0,-1]:
                    nr,nc = r+dr,c+dc
                    if (nr in range(rows) and nc in range(cols) and rooms[nr][nc] == inf):
                        rooms[nr][nc] = rooms[r][c] +1
                        q.append((nr,nc))

