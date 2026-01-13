# Last updated: 1/12/2026, 11:27:16 PM
1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3        res = []
4        subset = []
5
6        def dfs(l,r):
7            if len(subset) == 2*n:
8                res.append("".join(subset.copy()))
9                return
10            
11            if l < n:
12                subset.append("(")
13                dfs(l+1,r)
14                subset.pop()
15            
16            if r < l:
17                subset.append(")")
18                dfs(l,r+1)
19                subset.pop()
20        
21        dfs(0,0)
22        return res