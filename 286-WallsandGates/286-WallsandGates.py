# Last updated: 1/18/2026, 3:29:20 AM
1class Solution:
2    def wallsAndGates(self, rooms: List[List[int]]) -> None:
3        """
4        Do not return anything, modify rooms in-place instead.
5        """
6        inf = 2**31 - 1
7        rows,cols = len(rooms),len(rooms[0])
8        q = deque()
9
10        for r in range(rows):
11            for c in range(cols):
12                if rooms[r][c] == 0:
13                    q.append((r,c))
14        
15        while q:
16            r,c = q.popleft()
17            for dr,dc in [1,0],[-1,0],[0,1],[0,-1]:
18                nr,nc = r+dr,c+dc
19                if nr in range(rows) and nc in range(cols) and rooms[nr][nc] == inf:
20                    rooms[nr][nc] = rooms[r][c] + 1
21                    q.append((nr,nc))