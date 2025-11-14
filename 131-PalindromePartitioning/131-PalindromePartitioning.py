# Last updated: 11/14/2025, 5:02:20 PM
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        substring = []

        def dfs(i):
            if i == len(s):
                res.append(substring.copy())
                return 
            
            for j in range(i,len(s)):
                if self.ispal(i,j,s):
                    substring.append(s[i:j+1])
                    dfs(j+1)
                    substring.pop()
        
        dfs(0)
        return res


    def ispal(self,l,r,s):
        while l < r:
            if s[l] != s[r]:
                return False
            l = l +1
            r = r-1
        return True