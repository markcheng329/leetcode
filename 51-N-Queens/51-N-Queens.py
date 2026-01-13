# Last updated: 1/13/2026, 2:30:32 AM
1class Solution:
2    def solveNQueens(self, n: int) -> List[List[str]]:
3        col = set()
4        posdiag = set ()
5        nagdiag = set ()
6        res = []
7        board = [["."] * n for i in range(n)]
8
9        def dfs(r):
10            if r == n:
11                copy = ["".join(row) for row in board]
12                res.append(copy)
13                return
14            
15            for c in range(n):
16                if c in col or (r+c) in posdiag or (r-c) in nagdiag:
17                    continue
18                
19                col.add(c)
20                posdiag.add(r+c)
21                nagdiag.add(r-c)
22                board[r][c] = "Q"
23
24                dfs(r+1)
25                col.remove(c)
26                posdiag.remove(r+c)
27                nagdiag.remove(r-c)
28                board[r][c] = "."
29        dfs(0)
30        return res