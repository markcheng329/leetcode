# Last updated: 11/13/2025, 2:18:55 AM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = [[] for i in range(numCourses)]
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            
            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
                
            visit.remove(crs)
            preMap[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
