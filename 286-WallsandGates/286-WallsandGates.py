# Last updated: 1/18/2026, 3:39:00 AM
1class Solution:
2    def wallsAndGates(self, rooms: List[List[int]]) -> None:
3        """
4        Do not return anything, modify rooms in-place instead.
5        """
6        inf = 2**31 -1
7        rows,cols = len(rooms),len(rooms[0])
8        q = deque()
9        directions = [1,0],[-1,0],[0,1],[0,-1]
10
11        for r in range(rows):
12            for c in range(cols):
13                if rooms[r][c] == 0:
14                    q.append((r,c))
15        
16        while q:
17            r,c = q.popleft()
18            for dr,dc in directions:
19                nr,nc = r + dr, c + dc
20                if nr in range(rows) and nc in range(cols) and rooms[nr][nc] == inf:
21                    rooms[nr][nc] = rooms[r][c] + 1
22                    q.append((nr,nc))