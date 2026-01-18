# Last updated: 1/18/2026, 1:39:33 AM
1class Solution:
2    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
3        rows,cols = len(heights),len(heights[0])
4        pac,atl = set(),set()
5        res = []
6        directions = [1,0],[-1,0],[0,1],[0,-1]
7
8        def dfs(r,c,visited,prevHeight):
9            if r not in range(rows) or c not in range(cols) or (r,c) in visited or heights[r][c] < prevHeight:
10                return
11            
12            visited.add((r,c))
13            for dr, dc in directions:
14                dfs(r+dr,c+dc,visited,heights[r][c])
15        
16        for r in range(rows):
17            dfs(r,0,pac,heights[r][0])
18            dfs(r,cols-1,atl,heights[r][cols-1])
19        
20        for c in range(cols):
21            dfs(0,c,pac,heights[0][c])
22            dfs(rows-1,c,atl,heights[rows-1][c])
23
24        for r in range(rows):
25            for c in range(cols):
26                if (r,c) in pac and (r,c) in atl:
27                    res.append([r,c])
28        return res