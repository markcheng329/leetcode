# Last updated: 1/13/2026, 1:08:26 AM
1class Solution:
2    def partition(self, s: str) -> List[List[str]]:
3        res = []
4        subset = []
5
6        def dfs(i):
7            if i == len(s):
8                res.append(subset.copy())
9                return
10            
11            for j in range(i,len(s)):
12                if self.ispal(i,j,s) == True:
13                    subset.append(s[i:j+1])
14                    dfs(j+1)
15                    subset.pop()
16        
17        dfs(0)
18        return res
19    
20    def ispal(self,l,r,s):
21        while l < r:
22            if s[l] != s[r]:
23                return False
24            l +=1
25            r-=1
26        return True
27