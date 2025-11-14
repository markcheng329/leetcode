# Last updated: 11/14/2025, 5:43:51 PM
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posdiag = set()
        nagdiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def dfs(i):
            if i == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if (c in col or(i+c) in posdiag or (i-c) in nagdiag):
                    continue
                
                col.add(c)
                posdiag.add(i+c)
                nagdiag.add(i-c)
                board[i][c] = "Q"

                dfs(i+1)

                col.remove(c)
                posdiag.remove(i+c)
                nagdiag.remove(i-c)
                board[i][c] = "."
        dfs(0)
        return res
