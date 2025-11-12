# Last updated: 11/12/2025, 4:57:48 AM
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        res = 0
        visit = [False] * n

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            for nei in adj[node]:
                if visit[nei] == False:
                    visit[nei] = True
                    dfs(nei)
        
        for node in range(n):
            if visit[node] == False:
                visit[node] = True
                dfs(node)
                res +=1
        return res
        


        