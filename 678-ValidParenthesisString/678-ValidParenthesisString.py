# Last updated: 1/9/2026, 11:18:25 PM
1class Solution:
2    def checkValidString(self, s: str) -> bool:
3        lpmin = 0
4        lpmax = 0
5
6        for i in range(len(s)):
7            c = s[i]
8
9            if c == "(":
10                lpmin +=1
11                lpmax +=1
12            elif c == ")":
13                lpmin -=1
14                lpmax -=1
15            else:
16                lpmin -=1
17                lpmax +=1
18
19            if lpmax < 0:
20                return False
21            
22            if lpmin < 0:
23                lpmin =0
24        
25        return True if lpmin==0 else False
26
27            
28