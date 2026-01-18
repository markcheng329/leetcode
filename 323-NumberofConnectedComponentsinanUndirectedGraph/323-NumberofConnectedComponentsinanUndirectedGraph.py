# Last updated: 1/18/2026, 6:08:57 AM
1class Solution:
2    def countComponents(self, n: int, edges: List[List[int]]) -> int:
3        adj = [[] for i in range(n)]
4
5        res = 0
6        visit = [False] * n
7
8        for u,v in edges:
9            adj[u].append(v)
10            adj[v].append(u)
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