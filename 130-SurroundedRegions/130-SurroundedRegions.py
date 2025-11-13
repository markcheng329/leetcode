# Last updated: 11/13/2025, 2:12:45 AM
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows,cols = len(board),len(board[0])
        directions = [1,0],[-1,0],[0,1],[0,-1]

        def dfs(r,c):
            if (r not in range(rows) or c not in range(cols) or board[r][c] != "O"):
                return
            board[r][c] = "#"
            for dr,dc in directions:
                dfs(r+dr,c+dc)
        
        for r in range(rows):
            dfs(r,0)
            dfs(r,cols-1)
        
        for c in range(cols):
            dfs(0,c)
            dfs(rows-1,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "#":
                    board[r][c] = "O"