# Last updated: 1/13/2026, 12:25:28 AM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        rows = len(board)
4        cols = len(board[0])
5
6        def dfs(r,c,i):
7            if i == len(word):
8                return True
9            if r < 0 or r >= rows or c<0 or c>=cols or board[r][c] != word[i] or board[r][c] == "#":
10                return False
11            
12            board[r][c] = "#"
13            res = dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)
14            board[r][c] = word[i]
15            return res
16        
17        for r in range(rows):
18            for c in range(cols):
19                if dfs(r,c,0) == True:
20                    return True
21        return False