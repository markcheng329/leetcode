# Last updated: 1/19/2026, 11:47:39 PM
1class Solution:
2    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
3        pac,atl = set (),set()
4        directions = [1,0],[-1,0],[0,1],[0,-1]
5        rows,cols = len(heights),len(heights[0])
6        res = []
7        visited = set()
8
9        def dfs(r,c,visited,prevHeight):
10            if r not in range(rows) or c not in range(cols) or (r,c) in visited or heights[r][c] < prevHeight:
11                return
12            
13            visited.add((r,c))
14            for dr,dc in directions:
15                dfs(r+dr,c+dc,visited,heights[r][c])
16        
17        for r in range(rows):
18            dfs(r,0,pac,heights[r][0])
19            dfs(r,cols-1,atl,heights[r][cols-1])
20        
21        for c in range(cols):
22            dfs(0,c,pac,heights[0][c])
23            dfs(rows-1,c,atl,heights[rows-1][c])
24        
25        for r in range(rows):
26            for c in range(cols):
27                if (r,c) in atl and (r,c) in pac:
28                    res.append([r,c])
29        return res