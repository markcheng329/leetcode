# Last updated: 1/18/2026, 6:02:40 AM
1class Solution:
2    def countComponents(self, n: int, edges: List[List[int]]) -> int:
3        adj = [[] for i in range(n)]
4
5        for u,v in edges:
6            adj[u].append(v)
7            adj[v].append(u)
8        
9        visit = [False] * n
10
11        res = 0
12        
13        def dfs(node):
14            for nei in adj[node]:
15                if visit[nei] == False:
16                    visit[nei] = True
17                    dfs(nei)
18        
19        for node in range(n):
20            if visit[node] == False:
21                visit[node] = True
22                dfs(node)
23                res +=1
24        return res