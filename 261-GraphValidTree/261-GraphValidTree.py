# Last updated: 1/20/2026, 2:57:26 AM
1class Solution:
2    def validTree(self, n: int, edges: List[List[int]]) -> bool:
3        if len(edges) > n-1:
4            return False
5        
6        adj  = [[] for i in range(n)]
7
8        for u,v in edges:
9            adj[u].append(v)
10            adj[v].append(u)
11        
12        visit = set()
13
14        def dfs(node,parent):
15            if node in visit:
16                return False
17            
18            visit.add(node)
19            for nei in adj[node]:
20                if nei == parent:
21                    continue
22                if not dfs(nei,node):
23                    return False
24            return True
25        
26        return True if dfs(0,-1) and len(visit) == n else False
27