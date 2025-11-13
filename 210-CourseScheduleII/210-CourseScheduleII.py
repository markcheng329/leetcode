# Last updated: 11/13/2025, 3:25:45 AM
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = [[] for i in range(numCourses)]
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        
        cycle = set()
        visit = set()
        res = []

        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            preMap[crs] = []
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res

