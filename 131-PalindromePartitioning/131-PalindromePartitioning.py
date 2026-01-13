# Last updated: 1/13/2026, 12:55:29 AM
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
12                if self.ispal(i,j,s):
13                    subset.append(s[i:j+1])
14                    dfs(j+1)
15                    subset.pop()
16        dfs(0)
17        return res
18
19    
20
21
22
23    def ispal(self,l,r,s):
24        while l < r:
25            if s[l] != s[r]:
26                return False
27            
28            l +=1
29            r-=1
30        return True