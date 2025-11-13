# Last updated: 11/13/2025, 4:16:56 AM
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = [[] for i in range(len(edges)+1)]

        def dfs(node,parent):
            if visit[node] == True:
                return True
            
            visit[node] = True
            for nei in adj[node]:
                if nei == parent:
                    continue
                if dfs(nei,node) == True:
                    return True
            return False
        

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = [False] * ( len(edges) + 1)
            if dfs(u,-1) == True:
                return (u,v)
        return []
