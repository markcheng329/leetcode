# Last updated: 1/2/2026, 3:44:59 AM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        close_open = {")":"(","]":"[","}":"{"}
4        stack = []
5
6        for i in range(len(s)):
7            if s[i] in close_open:
8                if stack and close_open[s[i]] == stack[-1]:
9                    stack.pop()
10                else:
11                    return False
12            
13            else:
14                stack.append(s[i])
15        return True if not stack else False