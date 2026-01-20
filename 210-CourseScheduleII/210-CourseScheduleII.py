# Last updated: 1/20/2026, 12:24:28 AM
1class Solution:
2    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
3        preMap = [[] for i in range(numCourses)]
4        for crs,pre in prerequisites:
5            preMap[crs].append(pre)
6
7        visited,cycle = set(),set()
8        res = []
9
10        def dfs(crs):
11            if crs in cycle:
12                return False
13            
14            if crs in visited:
15                return True
16
17            cycle.add(crs)
18            for pre in preMap[crs]:
19                if not dfs(pre):
20                    return False
21            cycle.remove(crs)
22            visited.add(crs)
23            preMap[crs] = []
24            res.append(crs)
25            return True
26        
27        for c in range(numCourses):
28            if not dfs(c):
29                return []
30        return res
31            
32