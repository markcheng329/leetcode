# Last updated: 1/18/2026, 4:50:33 AM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        preMap = [[] for i in range(numCourses)]
4
5        for crs,pre in prerequisites:
6            preMap[crs].append(pre)
7
8        visit = set()
9
10        def dfs(crs):
11            if crs in visit:
12                return False
13            
14            visit.add(crs)
15            for pre in preMap[crs]:
16                if dfs(pre) != True:
17                    return False
18            
19            visit.remove(crs)
20            preMap[crs] = []
21            return True
22        
23        for i in range(numCourses):
24            if dfs(i) != True:
25                return False
26        return True
27        