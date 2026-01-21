# Last updated: 1/21/2026, 4:16:17 AM
1class Solution:
2    def validTree(self, n: int, edges: List[List[int]]) -> bool:
3
4        if len(edges) > n-1:
5            return False
6
7        adj = [[]for i in range(n)]
8
9        for u,v in edges:
10            adj[u].append(v)
11            adj[v].append(u)
12        
13        visited = set()
14
15        def dfs(node,parent):
16            if node in visited:
17                return False
18            
19            visited.add(node)
20            for nei in adj[node]:
21                if nei == parent:
22                    continue
23                if not dfs(nei,node):
24                    return False
25            return True
26        
27        return True if dfs(0,-1) and len(visited) == n else False
28
29
30
31