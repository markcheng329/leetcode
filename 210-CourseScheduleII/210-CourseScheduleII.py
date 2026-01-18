# Last updated: 1/18/2026, 4:59:51 AM
1class Solution:
2    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
3        preMap = [[] for i in range(numCourses)]
4
5        for crs,pre in prerequisites:
6            preMap[crs].append(pre)
7        
8        visit,cycle = set(),set()
9        res = []
10
11        def dfs(crs):
12            if crs in cycle:
13                return False
14            
15            if crs in visit:
16                return True
17            
18            cycle.add(crs)
19            for pre in preMap[crs]:
20                if not dfs(pre):
21                    return False
22            cycle.remove(crs)
23            visit.add(crs)
24            res.append(crs)
25            return True
26        
27        for i in range(numCourses):
28            if not dfs(i):
29                return []
30        return res
31        