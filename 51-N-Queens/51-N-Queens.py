# Last updated: 1/13/2026, 1:29:20 AM
1class Solution:
2    def solveNQueens(self, n: int) -> List[List[str]]:
3        col = set()
4        posdiag = set()
5        nagdiag = set()
6        res= []
7        board = [ ["."] * n for i in range(n)]
8
9        def dfs(r):
10            if r == n:
11                subset = ["".join(r) for r in board]
12                res.append(subset)
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
25
26                col.remove(c)
27                posdiag.remove(r+c)
28                nagdiag.remove(r-c)
29                board[r][c] = "."
30        
31        dfs(0)
32        return res
33