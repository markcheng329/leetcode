# Last updated: 11/12/2025, 4:58:10 AM
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = [[] for i in range(numCourses)]
        res = []
        cycle = set()
        visit = set()

        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        
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
            if dfs(i) == False:
                return []
        return res