# Last updated: 12/17/2025, 11:11:20 PM
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        cols = defaultdict(set)
4        rows = defaultdict(set)
5        squares = defaultdict(set)
6
7        for row in range(9):
8            for col in range(9):
9                if board[row][col] == ".":
10                    continue
11                
12                x = board[row][col] 
13
14                if x in cols[col] or x in rows[row] or x in squares[row//3,col//3]:
15                    return False
16                
17                rows[row].add(x)
18                cols[col].add(x)
19                squares[row//3,col//3].add(x)
20        return True