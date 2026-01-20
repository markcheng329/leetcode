# Last updated: 1/20/2026, 3:01:24 AM
1class Solution:
2    def countComponents(self, n: int, edges: List[List[int]]) -> int:
3        adj = [[] for i in range(n)]
4
5        for u,v in edges:
6            adj[u].append(v)
7            adj[v].append(u)
8        res = 0
9        
10        visit = [False] * n
11        
12        def dfs(node):
13            for nei in adj[node]:
14                if visit[nei] == False:
15                    visit[nei] = True
16                    dfs(nei)
17
18        for node in range(n):
19            if visit[node] == False:
20                visit[node] = True
21                dfs(node)
22                res +=1
23        return res
24