# Last updated: 12/11/2025, 2:06:37 AM
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        rows = defaultdict(set)
4        cols = defaultdict(set)
5        squares = defaultdict(set)
6
7        for r in range(9):
8            for c in range(9):
9                x = board[r][c] 
10                if x == ".":
11                    continue
12                if x in rows[r] or x in cols[c] or x in squares[r//3,c//3]:
13                    return False
14            
15                rows[r].add(x)
16                cols[c].add(x)
17                squares[r//3,c//3].add(x)
18        return True