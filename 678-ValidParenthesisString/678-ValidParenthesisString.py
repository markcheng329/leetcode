# Last updated: 1/11/2026, 3:59:49 AM
1class Solution:
2    def checkValidString(self, s: str) -> bool:
3        lpmin = 0
4        lpmax = 0
5
6        for i in range(len(s)):
7            if s[i] == "(":
8                lpmin +=1
9                lpmax +=1
10            elif s[i] == ")":
11                lpmin -=1
12                lpmax -=1
13            else:
14                lpmin -=1
15                lpmax +=1
16            
17            if lpmin < 0:
18                lpmin = 0
19            
20            if lpmax < 0:
21                return False
22        return True if lpmin==0 else False