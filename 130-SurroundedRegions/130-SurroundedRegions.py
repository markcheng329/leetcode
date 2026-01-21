# Last updated: 1/21/2026, 4:02:13 AM
1class Solution:
2    def solve(self, board: List[List[str]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        """
6        rows,cols = len(board),len(board[0])
7
8        def dfs(r,c):
9            if r not in range(rows) or c not in range(cols) or board[r][c] != "O":
10                return
11            
12            board[r][c] = "#"
13            for dr,dc in [1,0],[-1,0],[0,1],[0,-1]:
14                dfs(r+dr,c+dc)
15        
16        for r in range(rows):
17            dfs(r,0)
18            dfs(r,cols-1)
19        
20        for c in range(cols):
21            dfs(0,c)
22            dfs(rows-1,c)
23        
24        for r in range(rows):
25            for c in range(cols):
26                if board[r][c] == "O":
27                    board[r][c] = "X"
28                elif board[r][c] == "#":
29                    board[r][c] = "O"