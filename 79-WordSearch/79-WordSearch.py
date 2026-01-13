# Last updated: 1/13/2026, 12:16:51 AM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        rows,cols = len(board),len(board[0])
4
5        def dfs(r,c,i):
6            if i == len(word):
7                return True
8            
9            if r < 0 or c< 0 or r >= rows or c >= cols or board[r][c] != word[i] or board[r][c] == "#":
10                return False
11            
12            board[r][c] = "#"
13            res = dfs(r+1,c,i+1) or dfs(r,c+1,i+1) or dfs(r-1,c,i+1) or dfs(r,c-1,i+1)
14            board[r][c] = word[i]
15            return res
16
17
18        for r in range(rows):
19            for c in range(cols):
20                if dfs(r,c,0) == True:
21                    return True
22        return False