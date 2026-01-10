# Last updated: 1/9/2026, 11:18:54 PM
1class Solution:
2    def checkValidString(self, s: str) -> bool:
3        lmin,lmax = 0,0
4
5        for i in range(len(s)):
6            if s[i] == "(":
7                lmin +=1
8                lmax +=1
9            elif s[i] == ")":
10                lmin -=1
11                lmax -=1
12            else:
13                lmin -=1
14                lmax +=1
15        
16            if lmin < 0:
17                lmin = 0
18            
19            if lmax < 0:
20                return False
21                
22        return True if lmin == 0 else False