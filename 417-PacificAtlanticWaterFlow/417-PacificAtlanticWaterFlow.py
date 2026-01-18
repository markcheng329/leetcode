# Last updated: 1/18/2026, 1:28:01 AM
1class Solution:
2    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
3        rows = len(heights)
4        cols = len(heights[0])
5        res = []
6        pac = set()
7        atl = set()
8        directions = [1,0],[-1,0],[0,1],[0,-1]
9        
10        def dfs(r,c,visited,prevHeight):
11            if r not in range(rows) or c not in range(cols) or (r,c) in visited or heights[r][c] < prevHeight:
12                return
13            
14            visited.add((r,c))
15            for dr,dc in directions:
16                dfs(r+dr,c+dc,visited,heights[r][c])
17            
18        for r in range(rows):
19            dfs(r,0,pac,heights[r][0])
20            dfs(r,cols-1,atl,heights[r][cols-1])
21            
22        for c in range(cols):
23            dfs(0,c,pac,heights[0][c])
24            dfs(rows-1,c,atl,heights[rows-1][c])
25            
26        for r in range(rows):
27            for c in range(cols):
28                if (r,c) in pac and (r,c) in atl:
29                    res.append((r,c))
30        return res
31            