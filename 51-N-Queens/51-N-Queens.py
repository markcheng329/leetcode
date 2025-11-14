# Last updated: 11/14/2025, 5:54:45 PM
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posdiag = set()
        nagdiag = set()

        res= []
        board = [ ["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in nagdiag:
                    continue
            
                col.add(c)
                posdiag.add(r+c)
                nagdiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                posdiag.remove(r+c)
                nagdiag.remove(r-c)
                board[r][c] = "."
        
        backtrack(0)
        return res
