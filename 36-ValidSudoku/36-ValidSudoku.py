# Last updated: 12/27/2025, 12:30:12 AM
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        rows = defaultdict(set)
4        cols = defaultdict(set)
5        squares = defaultdict(set)
6
7        for row in range(9):
8            for col in range(9):
9                if board[row][col] == ".":
10                    continue
11                
12                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[row//3,col//3]:
13                    return False
14                
15                rows[row].add(board[row][col])
16                cols[col].add(board[row][col])
17                squares[row//3,col//3].add(board[row][col])
18        return True