# Last updated: 1/21/2026, 2:31:33 AM
1class Solution:
2    def wallsAndGates(self, rooms: List[List[int]]) -> None:
3        """
4        Do not return anything, modify rooms in-place instead.
5        """
6        inf = 2**31-1
7        rows,cols = len(rooms),len(rooms[0])
8        q = deque()
9
10        for r in range(rows):
11            for c in range(cols):
12                if rooms[r][c] == 0:
13                    q.append((r,c))
14        
15        while q:
16            for i in range(len(q)):
17                r,c = q.popleft()
18                for dr,dc in [1,0],[-1,0],[0,1],[0,-1]:
19                    nr,nc = r+dr,c+dc
20                    if nr in range(rows) and nc in range(cols) and rooms[nr][nc] == inf:
21                        rooms[nr][nc] = rooms[r][c] +1
22                        q.append((nr,nc))
23