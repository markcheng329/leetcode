# Last updated: 1/20/2026, 12:18:47 AM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        preMap = [[] for i in range(numCourses)]
4        for crs,pre in prerequisites:
5            preMap[crs].append(pre)
6        visited = set()
7        
8        def dfs(crs):
9            if crs in visited:
10                return False
11            
12            visited.add(crs)
13            for pre in preMap[crs]:
14                if not dfs(pre):
15                    return False
16            visited.remove(crs)
17            preMap[crs] = []
18            return True
19        
20        for i in range(numCourses):
21            if not dfs(i):
22                return False
23        return True
24