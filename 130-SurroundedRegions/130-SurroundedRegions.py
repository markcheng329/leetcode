# Last updated: 1/19/2026, 11:55:22 PM
1class Solution:
2    def solve(self, board: List[List[str]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        """
6        rows,cols = len(board),len(board[0])
7        directions = [1,0],[-1,0],[0,1],[0,-1]
8        
9        def dfs(r,c):
10            if r not in range(rows) or c not in range(cols) or board[r][c] != "O":
11                return
12            
13            board[r][c] = "#"
14            for dr,dc in directions:
15                dfs(r+dr,c+dc)
16        
17        for r in range(rows):
18            dfs(r,0)
19            dfs(r,cols-1)
20        
21        for c in range(cols):
22            dfs(0,c)
23            dfs(rows-1,c)
24        
25        for r in range(rows):
26            for c in range(cols):
27                if board[r][c] == "O":
28                    board[r][c] = "X"
29                elif board[r][c] == "#":
30                    board[r][c] = "O"
31                