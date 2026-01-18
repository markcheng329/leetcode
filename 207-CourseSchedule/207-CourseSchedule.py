# Last updated: 1/18/2026, 4:47:03 AM
1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        preMap = [[] for i in range(numCourses)]
4        for crs,pre in prerequisites:
5            preMap[crs].append(pre)
6        visit = set()
7
8        def dfs(crs):
9            if crs in visit:
10                return False
11            
12            visit.add(crs)
13            for pre in preMap[crs]:
14                if dfs(pre) != True:
15                    return False
16                
17            visit.remove(crs)
18            preMap[crs] = []
19            return True
20        
21        for i in range(numCourses):
22            if not dfs(i):
23                return False
24        return True
25